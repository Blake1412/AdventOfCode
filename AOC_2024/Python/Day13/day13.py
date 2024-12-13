from sys import argv
import numpy as np

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    games = [[int(g[2].split("+")[1][:-1]),
              int(g[3].split("+")[1]),
              int(g[6].split("+")[1][:-1]),
              int(g[7].split("+")[1]),
              int(g[9].split("=")[1][:-1]),
              int(g[10].split("=")[1]),
              ] for g in [game.split() for game in file.read().split("\n\n")]]

print(games)


def part1():
    total = 0
    for game in games:
        x = np.array([[game[0], game[2]], [game[1], game[3]]])
        y = np.array([game[4], game[5]])
        result = np.round(np.linalg.solve(x, y), 3)
        if result[0] % 1 == 0 and result[1] % 1 == 0:
            total += int(3 * result[0] + result[1])
    return total


def part2():
    total = 0
    for game in games:
        x = np.array([[game[0], game[2]], [game[1], game[3]]])
        y = np.array([game[4] + 10000000000000, game[5] + 10000000000000])
        result = np.round(np.linalg.solve(x, y), 3)
        if result[0] % 1 == 0 and result[1] % 1 == 0:
            total += int(3 * result[0] + result[1])
    return total


if __name__ == '__main__':
    timer(part1, part2)
