from day10.MapReader import MapReader


if __name__ == "__main__":
    with open("data/full_map", "r") as fh:
        asteroid_map = fh.read().splitlines()
    map_reader = MapReader(asteroid_map)
    map_reader.pairwise_angles()
    print(map_reader.visible_from_best)