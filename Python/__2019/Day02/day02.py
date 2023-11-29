from Python.__2019.intcode_computer import IntcodeComputer

with open("input.txt") as file:
    data = [int(x) for x in file.read().split(",")]


def part1():
    intcode_computer = IntcodeComputer(data)
    intcode_computer.registers[1] = 12
    intcode_computer.registers[2] = 2
    intcode_computer.run()
    return intcode_computer.registers[0]


def part2():
    for i in range(100):
        for j in range(100):
            intcode_computer = IntcodeComputer(data)
            intcode_computer.registers[1] = i
            intcode_computer.registers[2] = j
            intcode_computer.run()
            if intcode_computer.registers[0] == 19690720:
                return 100 * i + j


if __name__ == '__main__':
    print(part1())
    print(part2())
