import os
import numpy as np


def part1(txt):
    txt = txt.splitlines()
    txt = np.array(txt, dtype=np.int32)

    i = 0
    cnt = 0
    while i < len(txt) or i < 0:
        temp = i
        i += txt[temp]
        txt[temp] += 1
        cnt += 1
    return cnt


def part2(txt):
    txt = txt.splitlines()
    txt = np.array(txt, dtype=np.int32)

    i = 0
    cnt = 0

    while i < len(txt):
        temp = i
        i += txt[temp]
        if txt[temp] >= 3:
            txt[temp] -= 1
        else:
            txt[temp] += 1
        cnt += 1
        if cnt % 500000 == 0:
            print(cnt)
    return cnt


if __name__ == "__main__":
    with open("input/input_"+os.path.basename(__file__)+".txt") as f:
        val = f.read()

        print(part1(val))
        assert part1(val) == 358309

        print(part2("0\n3\n0\n1\n-3"))
        print(part2(val))
        # assert part2(val) == 251