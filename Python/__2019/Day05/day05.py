from Python.__2019.intcode_computer import IntcodeComputer

with open("input.txt") as file:
    data = [int(x) for x in file.read().split(",")]


def part1():
    intcode_computer = IntcodeComputer(data)
    intcode_computer.add_input(1)
    return intcode_computer.run_to_completion()[-1]


def part2():
    intcode_computer = IntcodeComputer(data)
    intcode_computer.add_input(5)
    return intcode_computer.run_to_completion()[-1]


if __name__ == '__main__':
    print(part1())
    print(part2())
