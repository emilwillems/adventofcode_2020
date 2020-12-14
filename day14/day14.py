from collections import defaultdict
from typing import List, Dict, Set

MEM_SIZE = 36

def apply_mask(m: str, v: int) -> int:
    binary = list(format(v, f"0{MEM_SIZE}b"))
    for i, c in enumerate(m):
        if c != 'X':
            binary[i] = c

    return int("".join(binary), 2)

def masked_addresses(start: int, mask: str) -> Set[int]:
    addr_base = list(format(start | int(mask.replace('X', '0'), 2), f"0{MEM_SIZE}b"))
    addr_list = set()
    x_count = mask.count('X')
    x_pos = [i for i, c in enumerate(mask) if c == 'X']

    for addr_mask in map(lambda num : format(num, f"0{x_count}b"), range(2**x_count)):
        addr_tmp = addr_base.copy()
        for index, bit in zip(x_pos, addr_mask):
            addr_tmp[index] = bit
        addr_list.add(int("".join(addr_tmp), 2))

    return addr_list

def execute(code: List[str], part=1) -> Dict[int, int]:
    mask = None
    memory = defaultdict(int)
    for l in code:
        tokens = l.split(" = ")
        if tokens[0] == "mask":
            mask = tokens[1]
        elif tokens[0].startswith("mem"):
            if mask is None:
                raise Exception("attemtpting to write memory without mask set")
            if part == 1:
                address, value = int(tokens[0][4:-1]), int(tokens[1])
                memory[address] = apply_mask(mask, value)
            elif part == 2:
                initial_addr, value = int(tokens[0][4:-1]), int(tokens[1])
                for addr in masked_addresses(initial_addr, mask):
                    memory[addr] = value
    return memory

def main(lines: List[str]) -> None:    
    print("part1:",sum(execute(lines, part=1).values()))
    print("part2:",sum(execute(lines, part=2).values()))

if __name__ == '__main__':
    main([l.rstrip() for l in open("day14/puzzle_input").readlines()])