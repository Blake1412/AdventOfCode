import sys

from Utils.utils import timer

with open(sys.argv[1]) as file:
    data = file.read().split("\n")

neighbours = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]


def part1():
    seen = set()
    total = 0
    for i, row in enumerate(data):
        for j, ch in enumerate(row):
            if not ch.isdigit() and ch != '.':
                for dx, dy in neighbours:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < len(data) and 0 <= y < len(row) and data[x][y].isdigit() and (x, y) not in seen:
                        seen.add((x, y))
                        number = get_full_number(x, y, seen)
                        total += int(number)
    return total


def part2():
    seen = set()
    total = 0
    for i, row in enumerate(data):
        for j, ch in enumerate(row):
            if not ch.isdigit() and ch == '*':
                part_numbers = []
                for dx, dy in neighbours:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < len(data) and 0 <= y < len(row) and data[x][y].isdigit() and (x, y) not in seen:
                        seen.add((x, y))
                        number = get_full_number(x, y, seen)
                        part_numbers.append(int(number))
                if len(part_numbers) == 2:
                    total += part_numbers[0] * part_numbers[1]
    return total


def get_full_number(x: int, y: int, seen: set):
    number = data[x][y]
    for yy in range(y - 1, -1, -1):
        if not data[x][yy].isdigit():
            break
        number = data[x][yy] + number
        seen.add((x, yy))
    for yy in range(y + 1, len(data[x])):
        if not data[x][yy].isdigit():
            break
        number += data[x][yy]
        seen.add((x, yy))
    return int(number)


if __name__ == '__main__':
    timer(part1, part2)
