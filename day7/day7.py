import re

BAG_TO_FIND = "shiny gold"

puzzle = [l.rstrip() for l in open("day7/puzzle_input").readlines()]

re_bags = re.compile(r"((\d+?) (.+?) bag)+")
bagsdict = dict()
for line in puzzle:
    (outside, inside) = line.split(" bags contain ")
    inside_bags = dict()
    bags_inside = re_bags.findall(inside)
    for bag in bags_inside:
        inside_bags[bag[2]] = int(bag[1])    
    bagsdict[outside] = inside_bags

# PART 1
bags_to_find = {BAG_TO_FIND}
found_bags = set()
while len(bags_to_find) > 0:
    find = bags_to_find.pop()    
    bags = [b for b, inside in bagsdict.items() if find in inside.keys()]
    bags_to_find.update(bags)
    found_bags.update(bags)

print(f"part1: {BAG_TO_FIND} can be in {len(found_bags)} outer bags.")

# PART 2
bags_count = 0
bags_to_process = [BAG_TO_FIND]
while len(bags_to_process) > 0:
    process = bags_to_process.pop()
    inside = bagsdict[process]
    for color, count in inside.items():
        bags_count += count
        bags_to_process.extend([color] * count)

print(f"part2: {BAG_TO_FIND} contains {bags_count} bags inside.")