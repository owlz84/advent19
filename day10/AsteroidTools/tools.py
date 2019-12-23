from typing import List, Type, Tuple
from collections import defaultdict
from math import sqrt, atan2, pi


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return self.x, self.y


class Asteroid:
    def __init__(self, coord: Coordinate):
        self._coord = coord
        self.pairwise_angles = set()

    def add_pairwise_angle(self, asteroid) -> None:
        theta = atan2(*self.delta(asteroid))
        self.pairwise_angles.add(theta)

    @property
    def coord(self):
        return self._coord()

    def delta(self, asteroid) -> Tuple[float, float]:
        x, y = asteroid.coord
        return self._coord.x - x, self._coord.y - y

    @property
    def n_visible_asteroids(self):
        return len(self.pairwise_angles)


class LaserGun:
    def __init__(self, location: Asteroid, asteroids: List[Asteroid], phase: float):
        self.location = location
        self.asteroids = asteroids
        self.phase = phase
        self.target_angles = defaultdict(list)

    def calc_target_angles(self):
        for asteroid in self.asteroids:
            dx, dy = self.location.delta(asteroid)
            theta = (atan2(dy, dx) + self.phase) % (2*pi)
            r = sqrt(dx**2 + dy**2)
            if not r == 0:
                asteroids = self.target_angles[theta]
                asteroids.append((r, asteroid))
                self.target_angles[theta] = sorted(asteroids)

    def destroy_them_with_lasers(self, n_shots: int):
        self.target_angles.clear()
        self.calc_target_angles()
        shots_fired = 0
        target = self.location
        done = False
        while not done:
            for theta in sorted(self.target_angles.keys()):
                r, target = self.target_angles[theta].pop(0)
                shots_fired += 1
                if shots_fired == n_shots:
                    done = True
                    break
        return target


class MapReader:
    def __init__(self, asteroid_map: List[str]):
        self.dims = (len(asteroid_map[0]), len(asteroid_map))
        self.asteroids = [
            Asteroid(Coordinate(colix, rwix)) for rwix, rw in enumerate(asteroid_map)
            for colix, val in enumerate(rw) if val == "#"
        ]

    def calc_pairwise_angles(self):
        for root_asteroid in self.asteroids:
            root_asteroid.pairwise_angles.clear()
            for asteroid in self.asteroids:
                if root_asteroid.coord != asteroid.coord:
                    root_asteroid.add_pairwise_angle(asteroid)

    @property
    def best_location(self):
        self.calc_pairwise_angles()
        return sorted(self.asteroids, key=lambda x: x.n_visible_asteroids)[-1]

    @property
    def translated_map(self):
        xdim, ydim = self.dims
        self.calc_pairwise_angles()
        all_pairwise_visible = defaultdict(int)
        for asteroid in self.asteroids:
            all_pairwise_visible[asteroid.coord] = asteroid.n_visible_asteroids
        return [[all_pairwise_visible[(x, y)] for x in range(xdim)] for y in range(ydim)]
