from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read().split()


def part1():
    total = 0
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for i in range(len(data)):
        for j in range(len(data)):
            for dx, dy in dirs:
                x, y = i, j
                word = data[i][j]
                for _ in range(3):
                    x = x + dx
                    y = y + dy
                    if len(data) > x >= 0 <= y < len(data[i]):
                        word += data[x][y]
                if word == "XMAS":
                    total += 1
    return total


def part2():
    total = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if data[i][j] == "A":
                word_one = data[i - 1][j - 1] + "A" + data[i + 1][j + 1]
                word_two = data[i - 1][j + 1] + "A" + data[i + 1][j - 1]
                if (word_one == 'SAM' or word_one == 'MAS') and (word_two == 'SAM' or word_two == 'MAS'):
                    total += 1
    return total


if __name__ == '__main__':
    timer(part1, part2)
