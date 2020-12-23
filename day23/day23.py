"""
adventofcode 2020, day 23
"""

class Node:
    """
    linked list node
    """
    def __init__(self, value):
        self.next = None
        self.value = value

    def __repr__(self):
        return str(self.value)

def build_list(numbers):
    """
    seed the linked list
    """
    nodes = {}
    prev = None
    for num in numbers:
        cur = Node(num)
        if prev:
            prev.next = cur
        prev = cur
        nodes[num] = cur

    # make it circular
    head = nodes[numbers[0]]
    prev.next = head
    return head, nodes

def play_rounds(head, nodes, rounds):
    """
    play the crabs cups game for {rounds} rounds
    """
    max_value = len(nodes)
    cur = head
    for _ in range(rounds):
        val = cur.value

        # get the three next nodes
        pick_1 = cur.next
        pick_2 = pick_1.next
        pick_3 = pick_2.next
        # separate nodes from list
        cur.next = pick_3.next

        # figure out the destination (if destination becomes 0, use max_value)
        destination = val - 1 or max_value
        while destination in (pick_1.value, pick_2.value, pick_3.value):
            destination = destination - 1 or max_value

        # relink the list and fit in the picked nodes
        dest_node = nodes[destination]
        pick_3.next = dest_node.next
        dest_node.next = pick_1
        cur = cur.next

    # return the node for cup with label 1
    return nodes[1]

def part_one(numbers):
    """
    play the game
    """
    list_head, list_nodes = build_list(numbers)
    node_one = play_rounds(list_head, list_nodes, 100)

    cur = node_one.next
    answer = ""
    while cur.value != 1:
        answer += str(cur.value)
        cur = cur.next

    return answer

def part_two(numbers):
    """
    play the real game
    """
    list_head, list_nodes = build_list(numbers)
    node_one = play_rounds(list_head, list_nodes, 10000000)
    return node_one.next.value * node_one.next.next.value

if __name__ == '__main__':
    cups_part_one = [int(n) for n in "219748365"]
    print("part1:", part_one(cups_part_one))
    cups_part_two = cups_part_one + list(range(max(cups_part_one) + 1, 1000001))
    print("part2:", part_two(cups_part_two))
