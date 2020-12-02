import re

input_lines = [line.rstrip() for line in open("puzzle_input", "r").readlines()]

valid_one = []
valid_two = []
spec_re = re.compile(r"^(\d+)-(\d+) ([a-z]): (.+)$")
for line in input_lines:
    m = spec_re.search(line)
    req_min, req_max, req_char, password = int(m[1]), int(m[2]), m[3], m[4]

    if req_min <= password.count(req_char) <= req_max:
        valid_one.append(password)
    if (password[req_min - 1] == req_char) ^ (password[req_max - 1] == req_char):
        valid_two.append(password)
    
print(f"part 1: {len(valid_one)} valid passwords")   
print(f"part 2: {len(valid_two)} valid passwords")   
