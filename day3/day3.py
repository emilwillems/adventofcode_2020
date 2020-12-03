import math

with open("day3/puzzle_input", "r") as file:
    treemap = [list(line.rstrip()) for line in file]


def traverse_map(the_map, step):
    pos = (0, 0)
    target_row = len(the_map) - 1
    tree_count = 0

    while(pos[1] < target_row):
        px, py = pos   
        dx, dy = step
        nx = (px + dx) % len(the_map[0])
        ny = py + dy
        pos = (nx, ny)    
        tree_count += the_map[ny][nx] == '#'

    return tree_count

print(f"part 1: Encountered {traverse_map(treemap, (3, 1))} trees!")

part2_steps = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]
part2_answer = math.prod([traverse_map(treemap, this_step) for this_step in part2_steps])
print(f"part 2: Traversed map with all steps, answer is {part2_answer}")

