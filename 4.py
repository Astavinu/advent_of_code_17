import os


def part1(txt):
    correct_lines = 0
    for line in txt.splitlines():
        words = line.split(" ")
        errors = 0
        for a in words:
            for b in words:
                if a == b:
                    errors += 1
        if errors <= len(words):
            correct_lines += 1
    return correct_lines


def part2(txt):
    correct_lines = 0
    for line in txt.splitlines():
        words = line.split(" ")
        errors = 0
        for a in words:
            for b in words:
                if sorted(a) == sorted(b):
                    errors += 1

        if errors <= len(words):
            correct_lines += 1
    return correct_lines


if __name__ == "__main__":
    with open("input/input_"+os.path.basename(__file__)+".txt") as f:
        val = f.read()
        print(part1(val))
        assert part1(val) == 466

        ex2 = part2(val)
        print(part2(val))
        assert part2(val) == 251