"""Simulate motor commands without connecting to physical hardware."""


def move(speed):
    print(f"  Motor: move forward at {speed:.1f} m/s")

def stop():
    print("  Motor: STOP")


if __name__ == "__main__":
    move(4.0)
    stop()
