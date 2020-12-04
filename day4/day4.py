import sys
import re

passports = open("day4/puzzle_input").read().split("\n\n")

# set to false for part 1
VALIDATE = True

# helpers for validation
VALID_ECL = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
re_hcl = re.compile("^#(?:[0-9a-fA-F]{6})$")
re_pid = re.compile("^(?:[0-9]{9})$")

def validate_byr(val):
    return 1920 <= int(val) <= 2020

def validate_iyr(val):
    return 2010 <= int(val) <= 2020

def validate_eyr(val):
    return 2020 <= int(val) <= 2030

def validate_hgt(val):
    m = val[-2:]
    if m == "cm":
        return 150 <= int(val[:-2]) <= 193
    elif m == "in":
        return 59 <= int(val[:-2]) <= 76
    else:
        return False

def validate_hcl(val):
    return re_hcl.search(val)
    
def validate_ecl(val):
    return val in VALID_ECL

def validate_pid(val):
    return re_pid.search(val)

valid_passports = 0
required_keys = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
for passport in passports:
    valid_keys = []
    pairs = passport.replace('/n', ' ').split()
    for pair in pairs:
        key, value = pair.split(':')
        if key in required_keys and key != 'cid':            
            if VALIDATE and not getattr(sys.modules[__name__], f"validate_{key}")(value):
                continue
            valid_keys.append(key)
    valid_passports += sorted(valid_keys) == required_keys
            
print(f"batch contained {valid_passports} 'valid' passports")
