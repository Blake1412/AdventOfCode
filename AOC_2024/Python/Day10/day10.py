from collections import deque
from sys import argv
from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = list(map(lambda row: [int(x) if x.isdigit() else x for x in row], file.read().split()))

neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def get_trails(start, end, reverse=False):
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == start:
                score = 0
                queue = deque()
                queue.append((i, j))
                seen = set()
                while queue:
                    x, y = queue.popleft()
                    seen.add((x, y))
                    if data[x][y] == end:
                        score += 1
                        continue
                    for dx, dy in neighbours:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < len(data) and 0 <= new_y < len(data[0]) and (new_x, new_y) not in seen:
                            if reverse and data[new_x][new_y] == data[x][y] - 1:
                                queue.append((new_x, new_y))
                            elif not reverse and data[new_x][new_y] == data[x][y] + 1:
                                queue.appendleft((new_x, new_y))
                total += score
    return total


def part1():
    return get_trails(0, 9)


def part2():
    return get_trails(9, 0, reverse=True)


if __name__ == '__main__':
    timer(part1, part2)
