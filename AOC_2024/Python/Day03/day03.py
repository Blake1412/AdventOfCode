from sys import argv
from re import findall

from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read()


def get_sum_mul_instructions(memory: str) -> int:
    instructions = findall(r"mul\((\d+),(\d+)\)", memory)
    return sum(list(map(lambda instruction: int(instruction[0]) * int(instruction[1]), instructions)))


def part1():
    return get_sum_mul_instructions(data)


def part2():
    global data
    data = data.split("do()")
    for idx, d in enumerate(data):
        location = d.find("don't()")
        if location > 0:
            data[idx] = d[:location]
    return get_sum_mul_instructions(str(data))


if __name__ == '__main__':
    timer(part1, part2)
