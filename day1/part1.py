
INPUTFILE = "day1/input"

puzzle_input = [int(l) for l in open(INPUTFILE, "r").readlines()]

def find_solution(puzzle):
    for pi1 in puzzle:
        for pi2 in puzzle:
            if pi1 + pi2 == 2020:
                return (pi1, pi2)
            
s1, s2 = find_solution(puzzle_input)
print(f"{s1} + {s2} = 2020, {s1} * {s2} = {s1 * s2}")
