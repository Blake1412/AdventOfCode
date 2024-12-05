from sys import argv
from collections import defaultdict
from functools import cmp_to_key

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read().split("\n\n")

rules = [(int(x), int(y)) for x, y in [rule.split("|") for rule in data[0].split()]]
updates = list(map(lambda x: [int(y) for y in x], [update.split(",") for update in data[1].split()]))

order_map = defaultdict(set)
for first, second in rules:
    order_map[first].add(second)


def part1():
    total = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(lambda x, y: -1 if y in order_map[x] else 1))
        if sorted_update == update:
            total += update[len(update) // 2]
    return total


def part2():
    total = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(lambda x, y: -1 if y in order_map[x] else 1))
        if not sorted_update == update:
            total += sorted_update[len(sorted_update) // 2]
    return total


if __name__ == '__main__':
    timer(part1, part2)
