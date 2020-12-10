from itertools import combinations

def get_invalid_number(numbers, preamble_length = 25):
    for i, n in enumerate(numbers[preamble_length:], start=preamble_length):
        if n not in {sum(pair) for pair in combinations(numbers[i - preamble_length:i], 2)}:
            return n
    raise Exception("no invalid number found")

def get_weakness(numbers, target_sum):
    slice_length = 2
    while slice_length < len(numbers) - slice_length:
        current_range = range(0, len(numbers)-slice_length+1)        
        slices = [numbers[current:current + slice_length] for current in current_range]
        for s in slices:
            if target_sum == sum(s):
                return min(s), max(s)
        slice_length += 1    
    raise Exception("no weakness found")

def main():
    numbers = [int(l) for l in open("day9/puzzle_input").readlines()]
    invalid = get_invalid_number(numbers, 25)
    print("part1:", invalid)
    weakness = get_weakness(numbers, invalid)
    print("part2: weakness =", weakness, "=> answer =", sum(weakness))

if __name__ == '__main__':
    main()