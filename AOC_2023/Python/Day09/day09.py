from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read().split("\n")


def part1():
    total_sum = 0
    for row in data:
        sequences = [[int(x) for x in row.split()]]
        cur_sequence = sequences[-1]
        while sum(cur_sequence) != 0:
            sequences.append([cur_sequence[i + 1] - cur_sequence[i] for i in range(len(cur_sequence) - 1)])
            cur_sequence = sequences[-1]
        sequences[-1].append(0)
        for i in range(len(sequences) - 2, -1, -1):
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
        total_sum += sequences[0][-1]
    return total_sum


def part2():
    total_sum = 0
    for row in data:
        sequences = [[int(x) for x in row.split()]]
        cur_sequence = sequences[-1]
        while sum(cur_sequence) != 0:
            sequences.append([cur_sequence[i + 1] - cur_sequence[i] for i in range(len(cur_sequence) - 1)])
            cur_sequence = sequences[-1]
        sequences[-1].insert(0, 0)
        for i in range(len(sequences) - 2, -1, -1):
            sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])
        total_sum += sequences[0][0]
    return total_sum


if __name__ == '__main__':
    timer(part1, part2)
