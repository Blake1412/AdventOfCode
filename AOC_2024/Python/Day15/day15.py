import copy
from collections import deque
from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data, movements = file.read().split("\n\n")
    data = [list(row) for row in data.split()]
    movements = movements.replace("\n", "")

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def get_connected_boxes(start, direction, grid):
    def process_box(x, y):
        if grid[x][y] == "#":
            return None
        elif grid[x][y] == "[":
            return (x, y), (x, y + 1)
        elif grid[x][y] == "]":
            return (x, y - 1), (x, y)
        return False

    boxes = deque([start])
    to_move = []
    dx, dy = direction

    while boxes:
        left, right = boxes.popleft()
        to_move.append((left, right))

        for x, y in [left, right]:
            new_box = process_box(x + dx, y)
            if new_box is None:
                return None
            elif new_box:
                boxes.append(new_box)

    return to_move


def part1():
    grid = copy.deepcopy(data)
    start_pos = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                start_pos = (i, j)
                grid[i][j] = "."

    total = 0
    current_pos = start_pos
    for movement in movements:
        x, y = current_pos
        dx, dy = directions[movement]
        ex, ey = nx, ny = x + dx, y + dy

        while grid[ex][ey] == "O":
            ex += dx
            ey += dy

        if grid[ex][ey] == "#":
            continue

        current_pos = (nx, ny)

        if (ex, ey) != current_pos:
            grid[ex][ey] = "O"
            grid[nx][ny] = "."

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                total += i * 100 + j
    return total


def part2():
    grid = ["#" * len(data[0]) * 2] * len(data)
    grid = [list(row) for row in grid]

    start_pos = (0, 0)
    for i in range(len(data)):
        for j in range(len(data[0])):
            char = data[i][j]
            if char == ".":
                grid[i][j * 2] = "."
                grid[i][j * 2 + 1] = "."
            elif char == "O":
                grid[i][j * 2] = "["
                grid[i][j * 2 + 1] = "]"
            elif char == "@":
                start_pos = (i, j * 2)
                grid[i][j * 2] = "."
                grid[i][j * 2 + 1] = "."

    total = 0
    current_pos = start_pos
    for movement in movements:
        x, y = current_pos
        dx, dy = directions[movement]
        nx, ny = x + dx, y + dy

        if grid[nx][ny] == ".":
            current_pos = (nx, ny)
            continue
        elif grid[nx][ny] == "#":
            continue

        if movement == "<" or movement == ">":
            ex, ey = nx, ny
            while grid[ex][ey] == "]" or grid[ex][ey] == "[":
                ex += dx
                ey += dy

            if grid[ex][ey] == "#":
                continue

            current_pos = (nx, ny)

            for k in range(ny, ey, dy):
                if grid[x][k] == "[":
                    grid[x][k] = "]"
                else:
                    grid[x][k] = "["

                grid[ex][ey] = "[" if movement == "<" else "]"
                grid[ex - dx][ey - dy] = "]" if movement == "<" else "["
                grid[nx][ny] = "."
        else:
            boxes = []
            if grid[nx][ny] == "]":
                boxes = get_connected_boxes(((nx, ny - 1), (nx, ny)), (dx, dy), grid)
            elif grid[nx][ny] == "[":
                boxes = get_connected_boxes(((nx, ny), (nx, ny + 1)), (dx, dy), grid)
            if not boxes:
                continue
            for box in reversed(boxes):
                (lx, ly), (rx, ry) = box
                grid[lx + dx][ly] = "["
                grid[rx + dx][ry] = "]"
                grid[lx][ly] = "."
                grid[rx][ry] = "."
            current_pos = (nx, ny)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                total += i * 100 + j
    return total


if __name__ == '__main__':
    timer(part1, part2)
