from collections import defaultdict
from math import lcm
from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read().split("\n")
    instruction_sequence = data[0]
    adj_list = defaultdict(list)
    for row in [row.split(" = ") for row in data[2:]]:
        adj_list[row[0]].extend(row[1][1:-1].split(", "))


def part1():
    start_node = "AAA"
    idx = 0
    steps = 0
    while start_node != "ZZZ":
        start_node = adj_list[start_node][0] if instruction_sequence[idx] == 'L' else adj_list[start_node][1]
        steps += 1
        idx = idx + 1 if idx != len(instruction_sequence) - 1 else 0
    return steps


def part2():
    start_nodes = []
    for k in adj_list:
        if k[-1] == 'A':
            start_nodes.append((k, 0))
    for i in range(len(start_nodes)):
        count = 0
        while start_nodes[i][0][-1] != 'Z':
            node = start_nodes[i][0]
            start_nodes[i] = (adj_list[node][0] if instruction_sequence[count] == "L" else adj_list[node][1], start_nodes[i][1] + 1)
            count = count + 1 if count != len(instruction_sequence) - 1 else 0
    return lcm(*[start_node[1] for start_node in start_nodes])


if __name__ == '__main__':
    timer(part1, part2)
