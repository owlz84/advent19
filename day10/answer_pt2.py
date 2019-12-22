from day10.MapReader import MapReader


if __name__ == "__main__":
    with open("data/full_map", "r") as fh:
        asteroid_map = fh.read().splitlines()
    x, y = (
        MapReader(asteroid_map)
        .calc_pairwise_angles()
        .calc_sweep_angles()
        .destroy_them_with_lasers(200)
    )
    print(100*x + y)
