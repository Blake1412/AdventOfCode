with open("input.txt") as file:
    data = [int(x) for x in file.read().split("\n")]


def part1():
    fuel = 0
    for module in data:
        fuel += module // 3 - 2
    return fuel


def part2():
    fuel = 0
    for module in data:
        while module > 6:
            module = module // 3 - 2
            fuel += module
    return fuel


if __name__ == '__main__':
    print(part1())
    print(part2())
