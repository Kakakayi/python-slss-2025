# AOC Day 1
# Karina Luo
# 1 Dec


def part_one():
    # read every line in the instructions
    counter = 50
    counter_zero = 0

    with open("data/aoc-2025.txt") as f:
        for line in f:
            # instruction example "R10" -> right 10
            direction = line[0]
            distance = int(line[1:])
            # if we go RIGHT --> add
            if direction == "R":
                counter += distance
                counter %= 100
                if counter == 0:
                    counter_zero += 1

            elif direction == "L":
                counter -= distance
                counter %= 100
                if counter == 0:
                    counter_zero += 1

        print(counter_zero)
        # if we go LEFT --> subtract
        # if we land on zero keep track of it
        # print how many times landed on 0


if __name__ == "__main__":
    part_one()
