
groups = open("day6/puzzle_input").read().split("\n\n")

part1 = 0
for group in groups:
    part1 += len({answer for person in [line.rstrip() for line in group.splitlines()] for answer in person})

print("part1:", part1)    
    
part2 = 0
for group in groups:    
    part2 += len(set.intersection(*[{answer for answer in person} for person in [line.rstrip() for line in group.splitlines()]]))

print("part2:", part2)
