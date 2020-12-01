INPUTFILE = "day1/input"

puzzle_input = set(int(l) for l in open(INPUTFILE, "r").readlines())

def find_solution(puzzle):
    for pi1 in puzzle:
        for pi2 in puzzle:
            if pi1 == pi2: 
                continue
            for pi3 in puzzle:
                if pi1 == pi3 or pi2 == pi3: 
                    continue
                if pi1 + pi2 + pi3 == 2020:
                    return (pi1, pi2, pi3)
            
s1, s2, s3 = find_solution(puzzle_input)
print(f"{s1} + {s2} + {s3} = 2020, {s1} * {s2} * {s3} = {s1 * s2 * s3}")
