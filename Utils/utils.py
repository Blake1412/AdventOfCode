import time


def timer(part1: callable, part2: callable):
    print("=====================================")
    now = time.time_ns()
    print("Part 1")
    print(f"Answer: {part1()}")
    total_time = time.time_ns() - now
    print("""Time: %.3fs""" % (total_time / 1e9))
    now = time.time_ns()
    print("=====================================")
    print("Part 2")
    print(f"Answer: {part2()}")
    total_time = time.time_ns() - now
    print("""Time: %.3fs""" % (total_time / 1e9))
    print("=====================================")


