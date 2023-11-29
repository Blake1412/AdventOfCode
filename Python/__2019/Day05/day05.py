from Python.__2019.intcode_computer import IntcodeComputer

with open("input.txt") as file:
    data = [int(x) for x in file.read().split(",")]


def part1():
    intcode_computer = IntcodeComputer(data)
    intcode_computer.input_data.append(1)
    intcode_computer.run()

    return intcode_computer.output_data.pop()


def part2():
    intcode_computer = IntcodeComputer(data)
    intcode_computer.input_data.append(5)
    intcode_computer.run()

    return intcode_computer.output_data.pop()


if __name__ == '__main__':
    print(part1())
    print(part2())
