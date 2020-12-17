from typing import Tuple, List, Set

CYCLES=6
ACTIVE='#'

def start_state(rows: List[str]) -> Set[Tuple[int, ...]]:
    active_cubes = {(x, y, 0, 0) for y, row in enumerate(rows) for x, part_one in enumerate(row) if part_one == ACTIVE}
    return active_cubes

def active_neighbour_count(state: Set[Tuple[int, ...]], x: int, y: int, z: int, w: int, use_w: bool = False) -> int:
    active_count = 0

    dw_range = (range(0, 1), range(-1, 2))[use_w]
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in dw_range:
                    # skip self
                    if dx == dy == dz == dw == 0:
                        continue
                    active_count += (x + dx, y + dy, z + dz, w + dw) in state

    return active_count

def do_cycle(pre_state: Set[Tuple[int, ...]], use_w: bool = False) -> Set[Tuple[int, ...]]:
    post_state = set()

    # get dimension sizes
    min_x = min_y = min_z = min_w = float('inf')
    max_x = max_y = max_z = max_w = float('-inf')
    for x, y, z, w in pre_state:
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
        min_z, max_z = min(min_z, z), max(max_z, z)
        min_w, max_w = min(min_w, w), max(max_w, w)

    # iterate over dimensions expanded by 1 (NOTE: range(a, b) actually goes from a to b - 1)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                for w in range(min_w - 1, max_w + 2):
                    # count neighbours and add to post_state active according to rules
                    anc = active_neighbour_count(pre_state, x, y, z, w, use_w)
                    if (x, y, z, w) in pre_state and anc in (2, 3):
                        post_state.add((x, y, z, w))
                    if (x, y, z, w) not in pre_state and anc == 3:
                        post_state.add((x, y, z, w))

    return post_state

if __name__ == '__main__':
    inp = [line.rstrip() for line in open("day17/puzzle_input").readlines()]
    part_one = start_state(inp)
    part_two = start_state(inp)
    for _ in range(CYCLES):
        part_one = do_cycle(part_one, use_w=False)
        part_two = do_cycle(part_two, use_w=True)

    print("part1:", len(part_one))
    print("part2:", len(part_two))
    