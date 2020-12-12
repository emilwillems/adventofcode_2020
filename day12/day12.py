#!/usr/bin/python

ANGLES = {
    0:      { "name": "north", "delta": (0, 1) },
    90:     { "name": "east", "delta": (1, 0) },
    180:    { "name": "south", "delta": (0, -1) },
    270:   { "name": "west", "delta": (-1, 0) }
}

DIRECTIONS = {"N": 0, "E": 90, "S": 180, "W": 270}

def get_md(position):
    return abs(position[0]) + abs(position[1])

commands = [l.rstrip() for l in open("day12/puzzle_input").readlines()]

angle = 90
position = [0, 0]
for c in commands:
    action = c[0]
    amount = int(c[1:])
    if action == "L":
        # rotate counterclockwise
        angle = (angle - amount) % 360
    elif action == "R":
        # rotate clockwise
        angle = (angle + amount) % 360
    elif action == "F":
        # move forward 
        position[0] += ANGLES[angle]['delta'][0] * amount
        position[1] += ANGLES[angle]['delta'][1] * amount
    else:
        # move in the direction specified
        position[0] += ANGLES[DIRECTIONS[action]]['delta'][0] * amount
        position[1] += ANGLES[DIRECTIONS[action]]['delta'][1] * amount
    
    print(f"{c}, now facing {angle} @ {position}")

print(f"part1: end position is {position}, manhatten distance: {get_md(position)}")
