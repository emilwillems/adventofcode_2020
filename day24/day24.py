"""
adventofcode 2020, day 24
"""
import re
from typing import Set, Tuple

DELTAS = {
    "e":    (1, -1, 0),
    "se":   (1, 0, -1),
    "sw":   (0, 1, -1),
    "w":    (-1, 1, 0),
    "nw":   (-1, 0, 1),
    "ne":   (0, -1, 1)
}

paths = [l.rstrip() for l in open("day24/puzzle_input", "r").readlines()]

active_tiles: Set[Tuple[int, int, int]] = set()
re_path = re.compile("(e|se|sw|sw|w|nw|ne)")
for p in paths:
    current = (0, 0, 0)
    for step in re_path.findall(p):
        current = (
            current[0] + DELTAS[step][0],
            current[1] + DELTAS[step][1],
            current[2] + DELTAS[step][2]
        )
    if current in active_tiles:
        active_tiles.remove(current)
    else:
        active_tiles.add(current)

print("part1:", len(active_tiles))

def get_neighbours(tile_list, xpos, ypos, zpos):
    """
    return a count of active tiles adjacent to given coords
    """
    count = 0
    for _, delta in DELTAS.items():
        count += (xpos + delta[0], ypos + delta[1], zpos + delta[2]) in tile_list
    return count

for day in range(100):
    new_state = active_tiles.copy()
    max_x = max(t[0] for t in active_tiles)
    min_x = min(t[0] for t in active_tiles)
    max_y = max(t[1] for t in active_tiles)
    min_y = min(t[1] for t in active_tiles)
    max_z = max(t[2] for t in active_tiles)
    min_z = min(t[2] for t in active_tiles)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                nb_count = get_neighbours(active_tiles, x, y, z)
                if (x, y, z) in active_tiles:
                    if nb_count == 0 or nb_count > 2:
                        new_state.remove((x, y, z))
                else:
                    if nb_count == 2:
                        new_state.add((x, y, z))
    active_tiles = new_state
    # print(f"Day {day+1}: {len(black_tiles)}")

print("part2:", len(active_tiles))
