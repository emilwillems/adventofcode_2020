"""
day 19 adventofcode 2020
"""
from collections import defaultdict

def parse_rules(unparsed):
    """
    parse the input into a dictionary
    """
    parsed = defaultdict(list)
    for rule in unparsed:
        rule_id, rule_content = rule.split(': ')
        for part in rule_content.split(' | '):
            if all(p.isnumeric() for p in part.split()):
                subrule = [int(n) for n in part.split() if n.isnumeric()]
                parsed[int(rule_id)].append(subrule)
            else:
                parsed[int(rule_id)] = part

    return parsed

def test(message, ruleset):
    """
    test if message matches any of the rules in ruleset
    """
    # if both message and ruleset are empty, return true, but return false
    # when only one of them is
    if message == "" or ruleset == []:
        return message == "" and ruleset == []

    rule = rules[ruleset[0]]
    # let's see if we match literal characters
    if '"' in rule:
        if message[0] in rule:
            return test(message[1:], ruleset[1:])
        return False

    # expand the first term of the first rule in the set and test it with
    # the rest of the set return true if any of them are okay
    return any(test(message, t + ruleset[1:]) for t in rule)

(text_rules, text_messages) = open("day19/puzzle_input").read().split("\n\n")
rules = parse_rules([r.strip() for r in text_rules.splitlines()])
messages = [m.strip() for m in text_messages.splitlines()]

# part 1
print("part1:", sum(test(m, [0]) for m in messages))

# part 2
rules[8] = [[42], [42,8]]
rules[11] = [[42,31], [42,11,31]]
print("part2:", sum(test(m, [0]) for m in messages))
