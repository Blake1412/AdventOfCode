import sys

from Utils.utils import timer

with open(sys.argv[1]) as file:
    data = [row.split(" ") for row in file.read().split("\n")]


def part1():
    total = 0
    for row in data:
        valid = True
        colors = {"red": 0, "green": 0, "blue": 0}

        for i in range(2, len(row), 2):
            for color in colors:
                if color in row[i + 1]:
                    colors[color] += int(row[i])

            if ";" in row[i + 1] or i == len(row) - 2:
                if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
                    valid = False
                    break
                colors = dict.fromkeys(colors, 0)

        if valid:
            total += int(row[1][:-1])

    return total


def part2():
    total = 0
    for row in data:
        colors = {"red": 0, "green": 0, "blue": 0}
        max_colors = {"red": 0, "green": 0, "blue": 0}
        for i in range(2, len(row), 2):
            for color in colors:
                if color in row[i + 1]:
                    colors[color] += int(row[i])
                    max_colors[color] = max(max_colors[color], colors[color])

            if ";" in row[i + 1] or i == len(row) - 2:
                colors = dict.fromkeys(colors, 0)

        total += max_colors["red"] * max_colors["green"] * max_colors["blue"]
    return total


if __name__ == '__main__':
    timer(part1, part2)
