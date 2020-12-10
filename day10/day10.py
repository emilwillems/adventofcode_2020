import collections

adapters = sorted([int(n) for n in open("day10/puzzle_input").readlines()])
adapters = [0] + adapters + [adapters[-1] + 3]

steps = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
counter = collections.Counter(steps)
print(f"part1: 1 diff = {counter[1]}, 3 diff = {counter[3]} ==> answer: {counter[1] * counter[3]}")

# possible routes to adapter value, seed with 1 route at 0 jolts
routes = {0: 1}
for joltage in adapters[1:]:
    # the number of routes to each joltage is the sum of the routes to up to three joltages below (max gap is 3)
    # 
    # if we have adapters with [0, 1, 2, 3, 5] joltages we can go 
    #   routes[0] to 1                          (= 1, after: routes = {0: 1, 1: 1})
    #   routes[1] + routes[0] to 2              (= 1 + 1, after: routes = {0: 1, 1: 1, 2: 2})
    #   routes[2] + routes[1] + routes[0] to 3  (= 2 + 1 + 1, after: routes = {0: 1, 1: 1, 2: 2, 3: 4})
    #   routes[4] + routes[3] + routes[2] to 5  (= 0 + 4 + 2, after: routes = {0: 1, 1: 1, 2: 2, 3: 4, 5: 6})
    #
    # we use dict.get with a default of 0 to fill in 'missing' adapters:
    routes[joltage] = routes.get(joltage - 1, 0) + routes.get(joltage - 2, 0) + routes.get(joltage - 3, 0)

print(f"part2: {routes[max(routes.keys())]}")
