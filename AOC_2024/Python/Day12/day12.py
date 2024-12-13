from collections import deque, defaultdict
from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read().split()

neighbours = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def part1():
    total = 0
    seen = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) not in seen:
                queue = deque()
                queue.append((i, j))
                seen.add((i, j))
                char = data[i][j]
                area, perimeter = 0, 0
                while queue:
                    x, y = queue.popleft()
                    area += 1
                    for dx, dy in neighbours:
                        new_x, new_y = x + dx, y + dy
                        if (new_x < 0 or new_x >= len(data) or new_y < 0 or new_y >= len(data[i])) or data[new_x][new_y] != char:
                            perimeter += 1
                        elif (new_x, new_y) not in seen:
                            queue.append((new_x, new_y))
                            seen.add((new_x, new_y))
                total += area * perimeter
    return total




def part2():
    total = 0
    seen = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) not in seen:
                queue = deque([(i, j)])
                seen.add((i, j))
                seen_perimeters = defaultdict(list)
                char = data[i][j]
                area, angles = 0, 0
                while queue:
                    x, y = queue.popleft()
                    area += 1
                    borders = [0, 0, 0, 0]
                    for idx, (dx, dy) in enumerate(neighbours):
                        nx, ny = x + dx, y + dy
                        if (nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[i])) or data[nx][ny] != char:
                            if (nx, ny) in seen_perimeters:
                                for other_x, other_y in seen_perimeters[nx, ny]:
                                    concave = True
                                    for dxx, dyy in neighbours:
                                        if (other_x, other_y) in seen_perimeters[(x + dxx, y + dyy)] and (x + dxx, y + dyy) != (nx, ny):
                                            concave = False
                                    if x != other_x and y != other_y and concave:
                                        angles += 1
                            seen_perimeters[(nx, ny)].append((x, y))
                            borders[idx] = 1
                        elif (nx, ny) not in seen:
                            queue.append((nx, ny))
                            seen.add((nx, ny))
                    angles += sum(borders[bx] and borders[by] for bx, by in [(0, 1), (0, 3), (2, 1), (2, 3)])
                total += area * angles
    return total


if __name__ == '__main__':
    timer(part1, part2)
