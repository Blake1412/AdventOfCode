from collections import defaultdict
from math import pow
from sys import argv

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    hands = [[row[0], int(row[1])] for row in [row.split() for row in file.read().split("\n")]]

ranks = {
    (1, 1, 1, 1, 1): 0,
    (1, 1, 1, 2): 1,
    (1, 2, 2): 2,
    (1, 1, 3): 3,
    (2, 3): 4,
    (1, 4): 5,
    (5,): 6
}

card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


def part1():
    total_score = 0
    hand_scores = [[*hand, 0] for hand in hands]
    for i, (hand, _, _) in enumerate(hand_scores):
        card_counts = defaultdict(int)
        for card in hand:
            card_counts[card] += 1
        hand_scores[i][2] = ranks[tuple(sorted(card_counts.values()))]
    hand_scores.sort(key=hand_key)
    for i, hand_score in enumerate(hand_scores):
        total_score += (i + 1) * hand_score[1]

    return total_score


def part2():
    card_values['J'] = 1
    total_score = 0
    hand_scores = [[*hand, 0] for hand in hands]
    for i, (hand, _, _) in enumerate(hand_scores):
        card_counts = defaultdict(int)
        for card in hand:
            card_counts[card] += 1

        for card, _ in sorted(card_counts.items(), key=lambda item: item[1], reverse=True):
            if card != 'J':
                card_counts[card] += card_counts['J']
                del card_counts['J']
                break
        hand_scores[i][2] = ranks[tuple(sorted(card_counts.values()))]
    hand_scores.sort(key=hand_key)
    for i, hand_score in enumerate(hand_scores):
        total_score += (i + 1) * hand_score[1]
    return total_score


def hand_key(hand: list[str, int, int]):
    cards, _, score = hand
    key = score * pow(14, 5 + 1)
    for i, card in enumerate(cards):
        key += card_values[card] * pow(14, 5 - i)
    return key


if __name__ == '__main__':
    timer(part1, part2)
