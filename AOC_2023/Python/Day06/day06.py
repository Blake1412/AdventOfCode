import sys

from Utils.utils import timer

with open(sys.argv[1] if len(sys.argv) > 1 else "data.txt") as file:
    times, distances = [row.split()[1:] for row in file.read().split("\n")]


def part1():
    total_count = 1
    for i, time in enumerate(times):
        distance = int(distances[i])
        time = int(time)
        count = 0

        for j in range(time):
            distance_travelled = j * (time - j)
            if distance_travelled > distance:
                count += 1
        total_count *= count
    return total_count


def part2():
    time = int("".join(times))
    distance = int("".join(distances))
    count = 0
    for j in range(time):
        distance_travelled = j * (time - j)
        if distance_travelled > distance:
            count += 1
    return count


if __name__ == '__main__':
    timer(part1, part2)
