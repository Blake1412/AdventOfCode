import sys
from math import pow

from Utils.utils import timer

with open(sys.argv[1]) as file:
    data = [[line[0].split(), line[1].split()] for line in [line.split("|") for line in [line.split(":")[1] for line in file.read().split("\n")]]]


def part1():
    total_score = 0
    for winning, player in data:
        matches = get_matches(winning, player)
        if matches:
            total_score += int(pow(2, matches - 1))
    return total_score


def part2():
    cards = [1] * len(data)
    for i, (winning, player) in enumerate(data):
        matches = get_matches(winning, player)
        for j in range(i + 1, i + matches + 1):
            cards[j] += cards[i]
    return sum(cards)


def get_matches(winning: list, player: list) -> int:
    matches = 0
    for number in player:
        if number in winning:
            matches += 1
    return matches


if __name__ == '__main__':
    timer(part1, part2)
