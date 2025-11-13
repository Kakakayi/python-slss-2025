# Maths Stuff with Python
# Author: Karina Luo
# 12 November 2025

import math

# Do math things with Python
# Machines are good at crunching numbers - faster
# and more accurately than most humans!


# Create a small program that calculates something useful
# to you (making you smile is useful).
def surface_area_of_cylider(r: int, h: int) -> float:
    # 2πrh+2πr**2
    return 2 * math.pi * r * h + 2 * math.pi * r**2


def main():
    print("What is the radius and height of the cylinder?")
    r = int(input("r: "))
    h = int(input("h: "))
    print(f"The surface area of the cylinder is: {surface_area_of_cylider(r, h)}!")


if __name__ == "__main__":
    main()
