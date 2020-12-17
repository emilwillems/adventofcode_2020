from typing import List, Set
import math

def part_one(valids: Set[int], tests: List[List[int]]) -> int:
    valids = [n for s in valids.values() for n in s]
    checksum = 0
    invalid_tests = list()
    for t in tests[1:]:
        for n in t:
            if n not in valids:
                checksum += n
                invalid_tests.append(t)

    for t in invalid_tests:
        tests.remove(t)
    return checksum

def part_two(valids: Set[int], tests: List[int]) -> int:
    to_find = {f: set() for f in valids.keys()}
    for i in range(len(tests[0])):
        valid_fields = set(valids.keys())
        for t in tests:
            valid_fields = set(f for f in valid_fields if t[i] in valids[f])
        for f in valid_fields:
            to_find[f].add(i)

    found = {}
    while len(to_find) > 0:
        for field in to_find:
            if len(to_find[field]) == 1:
                found[field] = to_find[field].pop()
                to_find.pop(field)
                for f in to_find:
                    to_find[f].remove(found[field])
                break

    return math.prod([tests[0][i] for field, i in found.items() if field.startswith("departure")])

def main(lines: List[str]) -> None:
    valid_set = dict()
    tickets = list()
    while len(lines) > 0:
        l = lines.pop(0).rstrip()
        if l == "" or l.endswith(":"):
            continue

        if ':' in l:
            valid_for_line = set()
            name, numbers = l.split(': ')
            for pair in numbers.split(' or '):
                low,high = [int(n) for n in pair.split('-')]
                valid_for_line.update(range(low, high+1))

            valid_set[name] = valid_for_line
        else:
            tickets.append([int(n) for n in l.split(',')])

    print("part1:", part_one(valid_set, tickets))
    print("part2:", part_two(valid_set, tickets))

if __name__ == '__main__':
    main(open("day16/puzzle_input", "r").readlines())
