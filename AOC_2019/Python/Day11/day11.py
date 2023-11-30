from collections import defaultdict

from AOC_2019.Python.intcode_computer import IntcodeComputer

with open("input.txt") as file:
    data = [int(x) for x in file.read().split(",")]


def part1():
    return len(run_robot('^'))


def part2():
    panels = run_robot('#')
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for panel in panels:
        x, y = panel
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    for i in range(min_y, max_y + 1):
        row = ""
        for j in range(min_x, max_x + 1):
            row += "#" if panels[(j, i)] == '#' else ' '
        print(row)


def run_robot(start: chr) -> defaultdict[tuple, chr]:
    panels = defaultdict(lambda: '^')
    panels[(0, 0)] = start
    position = (0, 0)
    direction = (0, 1)
    intcode_computer = IntcodeComputer(data)
    while True:
        intcode_computer.add_input(0 if panels[position] == '^' else 1)

        if not intcode_computer.run():
            paint = '#' if intcode_computer.output else '^'
        else:
            break

        if not intcode_computer.run():
            x, y = direction
            direction = (y, -x) if intcode_computer.output else (-y, x)
        else:
            break

        panels[position] = paint
        position = (position[0] + direction[0], position[1] - direction[1])
    return panels


if __name__ == '__main__':
    print(part1())
    part2()
