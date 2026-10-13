"""Decide whether the simulated AMR should move or stop using sensor data."""

from pathlib import Path

from motor.motor import move, stop
from sensor.lidar import get_distance
from sensor.camera import detect_person

ROOT = Path(__file__).resolve().parent.parent


def read_simple_settings(path):
    """Read simple key: value settings without third-party libraries."""
    settings = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, value = line.split(":", 1)
        settings[key.strip()] = value.strip()
    return settings


def main():
    motor_cfg = read_simple_settings(ROOT / "motor" / "motor_config.yaml")
    map_cfg = read_simple_settings(ROOT / "navigation" / "map.yaml")
    speed = float(motor_cfg["speed"])
    stop_distance = float(motor_cfg["stop_distance"])

    print(f"AMR simulation: {map_cfg['course_name']}")
    for step in range(1, int(map_cfg["steps"]) + 1):
        distance = get_distance(step)
        person = detect_person(step)
        print(f"Step {step}: LiDAR={distance:.1f} m, person={person}")
        if distance <= stop_distance or person:
            stop()
        else:
            move(speed)


if __name__ == "__main__":
    main()
