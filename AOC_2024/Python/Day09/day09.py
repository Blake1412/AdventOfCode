import copy
from sys import argv
from Utils.utils import timer

with open(argv[1] if len(argv) > 1 else "data.txt") as file:
    data = file.read()

files = []
space = []

i = 0
idx = 0
start = 0
while i < len(data):
    file_length = (int(data[i]))
    free_space = (int(data[i + 1])) if i + 1 < len(data) else 0
    files.append([[start, file_length]])
    if free_space:
        space.append([start + file_length, free_space])
    i += 2
    idx += 1
    start += file_length + free_space


def part1():
    total = 0
    files_copy = copy.deepcopy(files)
    space_copy = copy.deepcopy(space)

    file_idx = len(files_copy) - 1

    while space_copy[0][0] < files_copy[file_idx][0][0]:
        file_length = files_copy[file_idx][0][1]
        start, free_space = space_copy[0]

        if free_space >= file_length:
            files_copy[file_idx][0] = [start, file_length]
            if free_space == file_length:
                del space_copy[0]
            else:
                space_copy[0] = [start + file_length, free_space - file_length]
            file_idx -= 1

        else:
            files_copy[file_idx][0][1] -= free_space
            files_copy[file_idx].append([start, free_space])
            del space_copy[0]

    for idx, file_positions in enumerate(files_copy):
        for start, length in file_positions:
            total += sum(i * idx for i in range(start, start + length))
    return total


def part2():
    total = 0
    files_copy = copy.deepcopy(files)
    space_copy = copy.deepcopy(space)

    file_idx = len(files_copy) - 1

    while file_idx >= 0:
        file_length = files_copy[file_idx][0][1]

        for space_idx, (start, free_space) in enumerate(space_copy):
            if free_space >= file_length:
                break
        else:
            file_idx -= 1
            continue

        if start >= files_copy[file_idx][0][0]:
            file_idx -= 1
            continue

        if free_space > file_length:
            space_copy[space_idx] = [start + file_length, free_space - file_length]
            files_copy[file_idx][0] = [start, file_length]
        elif free_space == file_length:
            files_copy[file_idx][0] = [start, free_space]
            del space_copy[space_idx]

        file_idx -= 1

    for idx, file_positions in enumerate(files_copy):
        for file in file_positions:
            for i in range(file[0], file[0] + file[1]):
                total += i * idx
    return total


if __name__ == '__main__':
    timer(part1, part2)
