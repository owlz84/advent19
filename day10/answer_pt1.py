from day10.AsteroidTools import MapReader


if __name__ == "__main__":
    with open("data/full_map", "r") as fh:
        asteroid_map = fh.read().splitlines()
    print(MapReader(asteroid_map).best_location.n_visible_asteroids)
