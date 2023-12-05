from sys import argv

from Utils.utils import timer

with open(argv[1]) as file:
    data = file.read().split("\n\n")


def part1():
    seeds = [int(x) for x in data[0].split(": ")[1].split()]

    for range_mapping in data[1:]:
        conversions = {}
        for mapping in [row.split() for row in range_mapping.split("\n")[1:]]:
            destination, source, length = map(int, mapping)
            for seed in seeds:
                if source <= seed < source + length:
                    conversions[seed] = seed - (source - destination)
        for i, seed in enumerate(seeds):
            if seed in conversions:
                seeds[i] = conversions[seed]
    return min(seeds)


def part2():
    seeds = [int(x) for x in data[0].split(": ")[1].split()]
    seeds = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
    for range_mapping in data[1:]:
        conversions = {}
        for mapping in [row.split() for row in range_mapping.split("\n")[1:]]:
            destination, source, length = map(int, mapping)
            for i, (seed_start, seed_range) in enumerate(seeds):
                seed_end = seed_start + seed_range - 1
                source_end = source + length - 1
                diff_start = seed_start - source
                diff_end = seed_end - source_end

                if diff_start > 0 and diff_end > 0 and source_end > seed_start:
                    seeds[i][1] -= diff_end
                    seeds.append([seed_end - diff_end + 1, diff_end - 1])
                    conversions[seed_start] = destination + (seed_start - source)
                elif diff_start < 0 and diff_end < 0 and seed_end > source:
                    seeds[i][1] = source - seed_start - 1
                    seeds.append([source, seed_end - source])
                    conversions[source] = destination
                elif diff_start < 0 < diff_end:
                    seeds[i][1] = diff_start - 1
                    seeds.append([source, length])
                    seeds.append([source_end + 1, diff_end - 1])
                    conversions[source] = destination
                elif diff_start >= 0 >= diff_end:
                    conversions[seed_start] = destination + (seed_start - source)

        for i, (seed, _) in enumerate(seeds):
            if seed in conversions:
                seeds[i][0] = conversions[seed]

    return min([x[0] for x in seeds])


if __name__ == '__main__':
    timer(part1, part2)
