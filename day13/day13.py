import math

with open("day13/puzzle_input", "r") as fp:
    ts_arrival = int(fp.readline())
    buses = [c for c in fp.readline().split(",")]
fp.close()

# part 1
wait_times = dict()
for bus in buses:
    if bus == 'x':
        continue
    bus = int(bus)
    wait_times[bus] = bus - (ts_arrival % bus)

first_bus = min(wait_times, key=wait_times.get)
print(f"part1: bus {first_bus} comes first,", end=' ')
print(f"wait time is {wait_times[first_bus]} minutes,", end= ' ')
print(f"answer is {wait_times[first_bus] * first_bus}")

# part 2
ts = 0
step = 1
for offset, bus in enumerate(buses):
    if bus == 'x':
        continue
    bus_id = int(bus)
    while (ts + offset) % bus_id != 0:
        ts += step
    step *= bus_id

print (f"part2: all busses depart according to original schedule @ {ts}")
