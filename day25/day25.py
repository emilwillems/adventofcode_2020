"""
adventofcode 2020 day 25
"""
TEST = [5764801, 17807724]
PUZZLE = [6929599, 2448427]
MAGIC_NUMBER = 20201227

def transform(subject_number, loop_size):
    transform_result = 1
    for _ in range(loop_size):
        transform_result *= subject_number
        transform_result %= MAGIC_NUMBER

    return transform_result

def find_loop_size(key) -> int:
    initial_sn = 7
    result = 1
    loop_size = 0
    while result != key:
        result *= initial_sn
        result %= MAGIC_NUMBER
        loop_size += 1

    return loop_size


card_pub_key, door_pub_key = PUZZLE
card_loop_size = find_loop_size(card_pub_key)
door_loop_size = find_loop_size(door_pub_key)
print("part1:", transform(card_pub_key, door_loop_size))
