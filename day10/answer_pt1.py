from day10.MapReader import MapReader


if __name__ == "__main__":
    with open("data/full_map", "r") as fh:
        asteroid_map = fh.read().splitlines()
    print(
        MapReader(asteroid_map)
        .calc_pairwise_angles()
        .visible_from_best
    )
