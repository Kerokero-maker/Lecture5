"""Return simulated LiDAR distances in meters."""

DISTANCES = [3.0, 1.8, 0.6, 2.5]


def get_distance(step):
    return DISTANCES[(step - 1) % len(DISTANCES)]


if __name__ == "__main__":
    for step in range(1, 5):
        print(f"Step {step}: {get_distance(step):.1f} m")
