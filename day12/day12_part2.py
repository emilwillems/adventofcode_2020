#!/usr/bin/python

DIRECTIONS = {"N": 0, "E": 90, "S": 180, "W": 270}
DELTAS = {
    'N':     (0, 1),
    'E':    (1, 0),
    'S':   (0, -1),
    'W':   (-1, 0)
}

def get_md(position):
    return abs(position[0]) + abs(position[1])

def rotate(point, direction, amount):
    pos = point.copy()
    for i in range(0, amount, 90):
        new = [0,0]
        if direction == 'R':
            new[0] = pos[1]
            new[1] = pos[0] * -1
        if direction == 'L':
            new[0] = pos[1] * -1
            new[1] = pos[0]
        pos = new
    return pos

# start state
angle = 90
position = [0, 0]
waypoint = [10, 1]

commands = [l.rstrip() for l in open("day12/puzzle_input").readlines()]
for c in commands:
    action = c[0]
    amount = int(c[1:])
    if action == "L" or action == "R":
        # rotate
        waypoint = rotate(waypoint, action, amount)
    elif action == "F":
        # move towards waypoint
        position[0] += waypoint[0] * amount
        position[1] += waypoint[1] * amount
    else:
        # move the waypoint in the direction specified
        waypoint[0] += DELTAS[action][0] * amount
        waypoint[1] += DELTAS[action][1] * amount
    
print(f"part2: end position is {position}, manhatten distance: {get_md(position)}")
