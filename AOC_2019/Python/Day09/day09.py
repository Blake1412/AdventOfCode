from AOC_2019.Python.intcode_computer import IntcodeComputer

with open("input.txt") as file:
    data = [int(x) for x in file.read().split(",")]


def part1():
    intcode_computer = IntcodeComputer(data)
    intcode_computer.add_input(1)
    return intcode_computer.run_to_completion()[-1]


def part2():
    intcode_computer = IntcodeComputer(data)
    intcode_computer.add_input(2)
    return intcode_computer.run_to_completion()[-1]


print(part1())
print(part2())
