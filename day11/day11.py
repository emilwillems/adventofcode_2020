from collections import Counter
from copy import deepcopy

EMPTY = 'L'
TAKEN = '#'
FLOOR = '.'

DIRECTIONS = [
    (-1, -1), ( 0, -1), ( 1, -1),
    (-1,  0),           ( 1,  0),
    (-1,  1), ( 0,  1), ( 1,  1),  
]


def in_bounds(grid, x, y):
    return not (x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid))  

def do_round_part_one(grid):
    new = deepcopy(grid)

    for y, row in enumerate(grid):
        for x, spot in enumerate(row):
            state = [grid[y + delta[1]][x + delta[0]] for delta in DIRECTIONS if in_bounds(grid, x + delta[0], y + delta[1])]
            state_counter = Counter(state)
            if spot == EMPTY and TAKEN not in state_counter.keys():
                new[y][x] = TAKEN
            elif spot == TAKEN and state_counter[TAKEN] >= 4:
                new[y][x] = EMPTY
            else:
                new[y][x] = spot                        
    return new

def simulate(workload):
    iterations = 0
    while True:
        iterations += 1
        result = do_round_part_one(workload)
        if result == workload:
            return result, iterations
        else:
            workload = result

def main():
    puzzle = [list(l.rstrip()) for l in open("day11/puzzle_input").readlines()]
    result, count = simulate(puzzle)
    ct = Counter([spot for row in result for spot in row])
    print(f"result after {count} iterations:\n")
    for row in result:
        print("".join(row))
    print(f"\noccupied seats: {ct[TAKEN]}")
    
if __name__ == '__main__':
    main()