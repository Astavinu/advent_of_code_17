import os
import numpy as np


def part1(line):
    list = np.array(line.split("\t"), dtype=np.int32)

    def redist(list, i):
        cnt = list[i]

        for j in np.ones(cnt, dtype=np.int32):
            i += j
            i = i % cnt
            list[i] = list[i] + 1

    redist(list, 2)

    i = 0
    cnt = 0
    return cnt


def part2(line):
    pass


if __name__ == "__main__":
    with open("input/input_"+os.path.basename(__file__)+".txt") as f:
        val = f.readline()

        print(part1("0\t2\t7\t0"))
        # assert part1(val) == 358309

        print(part2(val))
        # assert part2(val) == 251