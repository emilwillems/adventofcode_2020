import sys
import os

from aoc2020 import aocrunner

def fix_code(program, index):
    """ 
    tries to fix the code by changing the first nop at or after index 
    to a jmp or vice versa

    returns a tuple with the 'fixed' code and the index of the changed
    instruction
    """
    lines = program.splitlines()
    for fixed, line in enumerate(lines):
        if fixed >= index:
            if line.startswith("nop"):
                lines[fixed] = line.replace("nop", "jmp")
                break
            elif line.startswith("jmp"):
                lines[fixed] = line.replace("jmp", "nop")
                break

    return ("\n".join(lines), fixed)

def part1():
    print("PART 1 - Running until infinite loop detected:")
    runner.load_program(code)
    try:
        runner.run()    
    except Exception as e:
            print(f"Execution halted due to {type(e).__name__}")
            print("!!",e)   
    runner.dump()   
    print()

def fix_code(program, fix_start):
    """ 
    tries to fix the code by changing the first nop at or after index 
    to a jmp or vice versa

    returns a tuple with the 'fixed' code and the index of the changed
    instruction
    """
    lines = program.splitlines()
    for fixed, line in enumerate(lines):
        if fixed >= fix_start:
            if line.startswith("nop"):
                lines[fixed] = line.replace("nop", "jmp")
                break
            elif line.startswith("jmp"):
                lines[fixed] = line.replace("jmp", "nop")
                break
    return ("\n".join(lines), fixed)

def part2():
    print("PART 2 - Trying to fix the code by changing nop's to jmp's (and vice versa)")
    fix_index = 0
    good_run = False
    while not good_run:
        fixed_code, fix_index = fix_code(code, fix_index)
        runner.load_program(fixed_code)
        try:
            runner.run()    
            good_run = True
        except aocrunner.InfiniteLoopException:
            fix_index += 1
    print(f"SUCCESS, fixed instruction at {fix_index}")
    runner.dump()
    print()

if __name__ == '__main__':
    runner = aocrunner.AOCRunner()
    code = open("day8/puzzle_input").read()
    part1()
    part2()
