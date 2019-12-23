from math import pi
from day10.AsteroidTools import MapReader, LaserGun


if __name__ == "__main__":
    with open("data/full_map", "r") as fh:
        asteroid_map = fh.read().splitlines()
    map_reader = MapReader(asteroid_map)
    x, y = (
        LaserGun(
            location=map_reader.best_location,
            asteroids=map_reader.asteroids,
            phase=-(pi/2)
        )
        .destroy_them_with_lasers(200)
        .coord
    )
    print(100*x + y)
