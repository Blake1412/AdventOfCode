import time

with open("data.txt") as file:
    data = file.read().split("\n")

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def part1():
    total = 0
    for row in data:
        string = ""
        temp = ""
        seen = False
        for ch in row:
            if ch.isdigit():
                temp = ch
                if not seen:
                    string += temp
                    seen = True
        string += temp
        total += int(string)
    return total


def part2():
    total = 0
    for row in data:
        string = ""
        temp_string = ""
        temp_char = ""
        seen = False
        for ch in row:
            if ch.isdigit():
                temp_char = ch
                temp_string = ""
                if not seen:
                    string += ch
                    seen = True
            else:
                temp_string += ch
                if not seen:
                    value = get_numeric_from_string(temp_string)
                    if value is not None:
                        string += value
                        seen = True
                        temp_string = ""

        string += value if (value := get_numeric_from_string(temp_string, True)) else temp_char
        total += int(string)
    return total


def get_numeric_from_string(string: str, last=False):
    if last:
        for i in range(len(string), 0, -1):
            for j in range(i - 1, -1, -1):
                substring = string[j:i]
                if substring in numbers:
                    return numbers[substring]
    else:
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                substring = string[i:j]
                if substring in numbers:
                    return numbers[substring]
    return None


if __name__ == '__main__':
    now = time.time_ns()
    print("Part 1")
    print(f"Answer: {part1()}")
    print(f"Time: {(time.time_ns() - now) // 1e+9}s")
    now = time.time_ns()
    print("Part 2")
    print(f"Answer: {part2()}")
    print(f"Time: {(time.time_ns() - now) // 1e+9}s")
