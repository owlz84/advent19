from typing import List
from collections import defaultdict
from math import sqrt, atan2, pi


class MapReader:
    def __init__(self, asteroid_map: List[str]):
        self.raw_map = asteroid_map
        self.dims = (len(asteroid_map[0]), len(asteroid_map))
        self.asteroids = [
            (colix, rwix) for rwix, rw in enumerate(asteroid_map)
            for colix, val in enumerate(rw) if val == "#"
        ]
        self.pairwise_angles = defaultdict(set)
        self.sweep_angles = defaultdict(list)

    @property
    def dx_dy(self):
        return [
            (x1, y1, x2, y2, x1-x2, y1-y2)
            for x1, y1 in self.asteroids
            for x2, y2 in self.asteroids
            if not (x1 == x2 and y1 == y2)
        ]

    def calc_pairwise_angles(self):
        self.pairwise_angles.clear()
        for x1, y1, x2, y2, dx, dy in self.dx_dy:
            theta = atan2(dy, dx)
            self.pairwise_angles[(x1, y1)].add(theta)
        return self
            
    def calc_sweep_angles(self):
        x0, y0 = self.best_location
        for x, y in self.asteroids:
            dx, dy = x0 - x, y0 - y
            theta = (atan2(dy, dx) - (pi/2)) % (2*pi)
            r = sqrt(dx**2 + dy**2)
            if not r == 0:
                asteroids = self.sweep_angles[theta]
                asteroids.append((r, (x, y)))
                self.sweep_angles[theta] = sorted(asteroids)
        return self

    @property
    def n_visible(self):
        return [(len(v), k) for k, v in self.pairwise_angles.items()]

    @property
    def best_location(self):
        return sorted(self.n_visible)[-1][1]

    @property
    def visible_from_best(self):
        return sorted(self.n_visible)[-1][0]

    @property
    def translated_map(self):
        xdim, ydim = self.dims
        return [[len(self.pairwise_angles[(x, y)]) for x in range(xdim)] for y in range(ydim)]

    def destroy_them_with_lasers(self, n_shots: int):
        shots_fired = 0
        coord = (0, 0)
        done = False
        while not done:
            for theta in sorted(self.sweep_angles.keys()):
                r, coord = self.sweep_angles[theta].pop(0)
                shots_fired += 1
                if shots_fired == n_shots:
                    done = True
                    break
        return coord
