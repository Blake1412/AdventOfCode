import time
start = time.perf_counter()
datastream = open("data.txt").readline()
print(f'Parsing = {(time.perf_counter() - start)}s')
start = time.perf_counter()


def part1():
    for i in range(len(datastream) - 4):
        if len(set(datastream[i:i + 4])) == 4:
            return i + 4


def part2():
    for i in range(len(datastream) - 14):
        if len(set(datastream[i:i + 14])) == 14:
            return i + 14


print(part1())
print(f'Part 1 = {(time.perf_counter() - start)}s')
start = time.perf_counter()
print(part2())
print(f'Part 2 = {(time.perf_counter() - start)}s')
