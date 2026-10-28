"""Simulate person detection without a physical camera."""


def detect_person(step):
    return step == 55


if __name__ == "__main__":
    for step in range(1, 5):
        print(f"Step {step}: person={detect_person(step)}")
