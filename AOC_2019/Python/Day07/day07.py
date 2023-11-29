from AOC_2019.Python.intcode_computer import IntcodeComputer
from itertools import permutations

with open("input.txt") as file:
    data = [int(x) for x in file.read().split(",")]


def part1():
    max_output = 0
    for phase_settings in permutations(range(5), 5):
        output = 0
        for phase_setting in phase_settings:
            intcode_computer = IntcodeComputer(data)
            intcode_computer.add_input(phase_setting, output)
            output = intcode_computer.run_to_completion()[-1]
        max_output = max(max_output, output)
    return max_output


def part2():
    max_output = 0
    for phase_settings in permutations(range(5, 10), 5):
        output = 0
        computers = [IntcodeComputer(data) for _ in range(5)]
        for i, phase_setting in enumerate(phase_settings):
            computers[i].add_input(phase_setting)
        running = True
        while running:
            running = False
            for intcode_computer in computers:
                intcode_computer.add_input(output)
                if not intcode_computer.run():
                    output = intcode_computer.output
                else:
                    break
            else:
                running = True
        max_output = max(max_output, output)

    return max_output


if __name__ == '__main__':
    print(part1())
    print(part2())
