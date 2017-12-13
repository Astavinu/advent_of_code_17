import os
import numpy as np


def part1(txt):
    sum = 0
    for line in txt.split("\n"):
        if line == '':
            continue
        num = line.split("\t")
        nums = np.array(num, dtype=np.int32)
        sum += max(nums) - min(nums)

    return sum


def part2(txt):
    sum = 0
    for line in txt.split("\n"):
        if line == '':
            continue
        num = line.split("\t")
        nums = np.array(num, dtype=np.int32)
        for i in nums:
            for j in nums:
                if i % j == 0 and i / j != 1:
                    sum += int(i / j)

    return sum


if __name__ == "__main__":
    with open("input/input_"+os.path.basename(__file__)+".txt") as f:
        val = f.read()
        # val = "5151"
        print(part1(val))
        print(part2(val))