import re

class Num:
    def __init__(self, val):
        self._val = val
    def __truediv__(self, other):
        return Num(self._val + other._val)
    def __mul__(self, other):
        return Num(self._val * other._val)
    def __sub__(self, other):
        return Num(self._val * other._val)        

def part_one(s):
    s = re.sub(r"(\d+)", r"Num(\1)", s)
    s = re.sub(r"[+]", r'/', s)
    return eval(s)._val

def part_two(s):
    s = re.sub(r"(\d+)", r"Num(\1)", s)
    s = re.sub(r"[+]", r'/', s)
    s = re.sub(r"[*]", r'-', s)
    return eval(s)._val

lines = open('day18/puzzle_input').readlines()
print(sum(part_one(line.strip()) for line in lines))
print(sum(part_two(line.strip()) for line in lines))
