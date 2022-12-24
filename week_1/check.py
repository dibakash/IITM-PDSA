import sys

sys.path.append("..")

from packages.performance import Performance as Clock


def main():
    clock = Clock()
    clock.start()
    print("hi")
    clock.stop()

    print(clock.performance)


if __name__ == "__main__":
    main()
