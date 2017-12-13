import os
import numpy as np


def part1(number):
    number = int(number)
    direction = 1
    line_count = 1
    dy = 0
    dx = 0
    n = 1

    while n < number:
        for x in range(line_count):
            dx += direction
            n += 1
            if n == number:
                return abs(dy) + abs(dx)

        for y in range(line_count):
            dx += direction
            n += 1
            if n == number:
                return abs(dy) + abs(dx)

        direction *= -1
        line_count += 1

    return


def part2(number):
    field = {}
    number = int(number)

    def put_num(n, x, y):
        field.update({"{0},{1}".format(x,y): n})

    def get_num(x, y):
        return field.get("{0},{1}".format(x, y))

    def sum_neighbors(x, y):
        offset = [[-1,-1], [-1, 0], [0, -1], [-1, 1], [1, -1], [0, 1], [1, 0], [1, 1]]
        neighbors = [get_num(x + o[0], y + o[1]) for o in offset]
        neighbors = [n for n in neighbors if n is not None]
        return sum(neighbors)

    put_num(1, 0, 0)

    x = 0
    y = 0
    direction = 1
    line_count = 1
    n = 0

    while n <= number:

        for dx in range(line_count):
            x += direction
            n = sum_neighbors(x, y)
            put_num(n, x, y)

            if n > number:
                return n

        for dy in range(line_count):
            y += direction
            n = sum_neighbors(x, y)
            put_num(n, x, y)

            if n > number:
                return n

        direction *= -1
        line_count += 1

    return n


if __name__ == "__main__":
    with open("input/input_"+os.path.basename(__file__)+".txt") as f:
        val = f.read()
        # val = "362"
        print(part1(val))
        print(part2(val))
