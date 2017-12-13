import os

def part1(number):
    last = number[-1]
    sum = 0

    for c in number:
        if last == c:
            sum += int(c)
        last = c
    return sum


def part2(number):
    sum = 0
    for i in range(len(number)):
        a = int(number[i])
        j = int(i+len(number)/2)%len(number)
        b = int(number[j])

        if a == b:
            sum += a
    return sum


if __name__ == "__main__":
    with open("input/input_"+os.path.basename(__file__)+".txt") as f:
        val = f.read()
        # val = "5151"
        print(part1(val))
        print(part2(val))