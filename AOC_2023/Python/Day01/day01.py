import sys

from Utils.utils import timer

with open(sys.argv[1]) as file:
    data = file.read().split("\n")

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def part1():
    total = 0
    for row in data:
        total += int("".join(get_numerics_from_string(row)))
    return total


def part2():
    total = 0
    for row in data:
        total += int("".join(get_numerics_from_string(row, include_strings=True)))
    return total


def get_numerics_from_string(string: str, include_strings=False):
    first_last = [None, None]
    i = 0

    while not first_last[0]:
        if string[i].isdigit():
            first_last[0] = string[i]
        elif include_strings:
            for j in range(i + 1, len(string) + 1):
                if string[j - 1].isdigit():
                    break
                if string[i:j] in numbers:
                    first_last[0] = numbers[string[i:j]]
        i += 1

    i = len(string)
    while not first_last[1]:
        if string[i - 1].isdigit():
            first_last[1] = string[i - 1]
        elif include_strings:
            for j in range(i - 1, -1, -1):
                if string[j].isdigit():
                    break
                if string[j:i] in numbers:
                    first_last[1] = numbers[string[j:i]]
        i -= 1

    return first_last


if __name__ == '__main__':
    timer(part1, part2)
