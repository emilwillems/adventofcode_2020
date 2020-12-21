"""
solutions for day 21 of adventofcode 2020
"""
from typing import DefaultDict, Any, Set
from collections import defaultdict

import re

lines = [l.rstrip() for l in open("day21/puzzle_input").readlines()]

word_frequency: DefaultDict[str, int] = defaultdict(int)
translations: DefaultDict[str, Set[str]] = defaultdict(set)
re_line = re.compile(r'(.*) \(contains (.*)\)')
for line in lines:
    matches: Any = re_line.match(line)
    ingredients = matches.group(1).split()
    allergens = matches.group(2).split(', ')
    for i in ingredients:
        word_frequency[i] += 1
    for a in allergens:
        if a not in translations:
            translations[a] = set(ingredients)
        else:
            translations[a] = translations[a].intersection(ingredients)


# part 1
allergens = set()
for p in translations.values():
    allergens.update(p)
print("part1:", sum(word_frequency[i] for i in word_frequency.keys() - allergens))

# part two
print(translations)
translated: DefaultDict[str, str] = defaultdict(str)
to_find = set(translations.keys())
while len(to_find) > 0:
    for f in to_find:
        print(f"looking for '{f}'")
        if len(translations[f]) == 1:
            found = translations[f].pop()
            print (f" >> translation found: '{found}'")
            translated[f] = found
            for allergen, options in translations.items():
                if found in options:
                    print(f" !! removing '{found}' as option for '{allergen}'")
                    translations[allergen].remove(found)
            to_find.remove(f)
            break

print ("part2:", ",".join([translated[k] for k in sorted(translated)]))
