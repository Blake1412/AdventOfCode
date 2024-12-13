from sys import argv
from Utils.utils import timer
from collections import defaultdict

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    stones = file.read().split()

def get_length_after_iterations(iterations):
    freqs = defaultdict(int)
    for stone in stones:
        freqs[stone] += 1

    for _ in range(iterations):
        next_freqs = defaultdict(int)
        for stone, freq in freqs.items():
            if stone == '0':
                next_freqs['1'] += freq
            elif len(stone) % 2 == 0:
                half = len(stone) // 2
                first_half = stone[:half].lstrip("0") or "0"
                second_half = stone[half:].lstrip("0") or "0"
                next_freqs[first_half] += freq
                next_freqs[second_half] += freq
            else:
                new_stone = str(int(stone) * 2024)
                next_freqs[new_stone] += freq
        freqs = next_freqs

    return sum(freqs.values())



def part1():
    return get_length_after_iterations(25)


def part2():
    return get_length_after_iterations(75)


if __name__ == '__main__':
    timer(part1, part2)
