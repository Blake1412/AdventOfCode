from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read().split()

start = (0, 0)
for row_idx, row in enumerate(data):
    for col_idx, col in enumerate(row):
        if col == '^':
            start = (row_idx, col_idx)


def part1():
    seen = set()
    direction = (-1, 0)
    cur_pos = start
    while True:
        x, y = cur_pos
        dx, dy = x + direction[0], y + direction[1]
        if dx < 0 or dx >= len(data) or dy < 0 or dy >= len(data[0]):
            seen.add(cur_pos)
            break
        while data[dx][dy] == '#':
            direction = (direction[1], -direction[0])
            dx, dy = x + direction[0], y + direction[1]
        seen.add(cur_pos)
        cur_pos = (dx, dy)
    return len(seen)


def find_loop():
    seen = set()
    direction = (-1, 0)
    cur_pos = start
    while True:
        x, y = cur_pos
        dx, dy = x + direction[0], y + direction[1]
        if dx < 0 or dx >= len(data) or dy < 0 or dy >= len(data[0]):
            return False
        while data[dx][dy] == '#':
            direction = (direction[1], -direction[0])
            dx, dy = x + direction[0], y + direction[1]
            if dx < 0 or dx >= len(data) or dy < 0 or dy >= len(data[0]):
                return False
        if ((dx, dy), direction) in seen:
            return True
        seen.add(((dx, dy), direction))
        cur_pos = (dx, dy)


def part2():
    count = 0

    for i, row in enumerate(data):
        row_copy = row
        for j, col in enumerate(row):
            if col != "^" and col != '#':
                data[i] = row[:j] + '#' + row[j + 1:]
                if find_loop():
                    count += 1
            data[i] = row_copy
    return count


if __name__ == '__main__':
    timer(part1, part2)
