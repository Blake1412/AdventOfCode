import statistics
from collections import defaultdict, deque
from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    robots = [[
        int(robot[0].split(",")[0].split("=")[1]),
        int(robot[0].split(",")[1]),
        int(robot[1].split(",")[0].split("=")[1]),
        int(robot[1].split(",")[1])
    ] for robot in [row.split() for row in file.read().split("\n")]]

height, width = 103, 101
grid = ["." * width] * height


def part1():
    positions = defaultdict(list)
    for idx, (x, y, _, _) in enumerate(robots):
        positions[idx] = [x, y]

    for i in range(100):
        for idx, (_, _, dx, dy) in enumerate(robots):
            nx = (positions[idx][0] + dx) % width
            ny = (positions[idx][1] + dy) % height
            positions[idx] = [nx, ny]

    quadrants = [0, 0, 0, 0]

    for x, y in positions.values():
        if x < width // 2 and y < height // 2:
            quadrants[0] += 1
        elif x > width // 2 and y < height // 2:
            quadrants[1] += 1
        elif x < width // 2 and y > height // 2:
            quadrants[2] += 1
        elif x > width // 2 and y > height // 2:
            quadrants[3] += 1

    total = 1
    for quadrant in quadrants:
        total *= quadrant
    return total


def part2():
    idx = 0
    while True:
        idx += 1
        positions = set()
        for i, (x, y, dx, dy) in enumerate(robots):
            nx = (x + dx) % width
            ny = (y + dy) % height
            robots[i] = [nx, ny, dx, dy]
            positions.add((nx, ny))

        if len(positions) == len(robots):
            return idx


if __name__ == '__main__':
    timer(part1, part2)
