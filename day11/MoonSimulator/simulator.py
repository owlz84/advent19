from __future__ import annotations
import re
from typing import List
from pprint import PrettyPrinter
from copy import deepcopy
from math import gcd

MOONS = ["io", "europa", "ganymede", 'callisto']
SENSOR_FORMAT = r"^<.*=(?P<x>-?\d*).*=(?P<y>-?\d*).*=(?P<z>-?\d*)>$"
DIMENSIONS = ["x", "y", "z"]
PP = PrettyPrinter()


def lcm(x, y):
    return x * y // gcd(x, y)


class Moon:
    def __init__(self, name, position: list, velocity: list):
        self.name = name
        self.position = position
        self.initial_position = position
        self.velocity = velocity

    def gravity(self, other_position):
        gravity_vector = []
        for v1, v2 in zip(self.position, other_position):
            if v1 < v2:
                gravity = 1
            elif v1 > v2:
                gravity = -1
            else:
                gravity = 0
            gravity_vector.append(gravity)
        return gravity_vector

    def update_velocity(self, moons):
        for moon in moons:
            if not moon.name == self.name:
                self.velocity = [v1 + v2 for v1, v2 in zip(self.velocity, self.gravity(moon.position))]

    def update_position(self, moons):
        self.update_velocity(moons)
        self.position = [v1 + v2 for v1, v2 in zip(self.position, self.velocity)]

    @property
    def potential_energy(self):
        return sum([abs(val) for val in self.position])

    @property
    def kinetic_energy(self):
        return sum([abs(val) for val in self.velocity])

    @property
    def energy(self):
        return self.potential_energy * self.kinetic_energy

    def __str__(self):
        return PP.pformat(dict(
            name=self.name,
            position=self.position,
            velocity=self.velocity
        ))


class Simulator:
    def __init__(self, sensor_data: List[str]):
        self.t = 0
        self.output_interval = 10
        self.total_energy = 0
        self.system_periods = [-1, -1, -1]
        matcher = re.compile(SENSOR_FORMAT)
        self.moons = [
            Moon(
                name=MOONS[ix],
                position=[int(val) for val in matcher.match(observation).groups()],
                velocity=[0, 0, 0]
            )
            for ix, observation in enumerate(sensor_data)
        ]
        self.system_initial_positions = [[moon.position[i] for moon in self.moons] for i in range(len(DIMENSIONS))]
        self.system_initial_velocities = [[moon.velocity[i] for moon in self.moons] for i in range(len(DIMENSIONS))]

    def step(self):
        output_flag = (self.t % self.output_interval == 0)
        original_states = deepcopy(self.moons)
        self.total_energy = 0
        if output_flag:
            print(f"values at time: {self.t}")
        for moon in self.moons:
            self.total_energy += moon.energy
            if output_flag:
                print(moon)
            moon.update_position(original_states)
        if output_flag:
            print(f"total energy : {self.total_energy}")
        self.t += 1

    def run(self, n_steps):
        for i in range(n_steps + 1):
            self.step()

    def find_periods(self):
        while True:
            self.step()
            for dim in range(len(DIMENSIONS)):
                current_positions = [moon.position[dim] for moon in self.moons]
                current_velocities = [moon.velocity[dim] for moon in self.moons]
                if current_positions == self.system_initial_positions[dim] \
                    and current_velocities == self.system_initial_velocities[dim] \
                    and self.system_periods[dim] == -1:
                    self.system_periods[dim] = self.t
            if all([period > -1 for period in self.system_periods]):
                break

    @property
    def system_period(self):
        self.find_periods()
        result = 1
        for period in self.system_periods:
            result = lcm(result, period)
        return result
