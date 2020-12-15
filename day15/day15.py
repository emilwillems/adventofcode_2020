from typing import List
from collections import defaultdict

test = "0,3,6"
puzzle = "1,0,15,2,10,13"

numbers = [int(x) for x in puzzle.split(',')]

def speak(turn: int, number: int, state: List[int]) -> None:
    # print (f"Turn {turn}: number spoken is {number}")
    state[number].insert(0, turn)
    if len(state[number]) > 2:
        state[number].pop(-1)
    

def play(numbers: List[int], break_at: int=10) -> int:
    spoken = defaultdict(list)
    turn = 1
    last_spoken = None

    # intitialize game with starting numbers
    while len(numbers) > 0:
        nr = numbers.pop(0)
        speak(turn, nr, spoken)
        turn += 1
        last_spoken = nr

    while True:        
        if len(spoken[last_spoken]) == 1:
            # this was the first time the number was spoken
            round_number = 0
        elif last_spoken in spoken:
            round_number = spoken[last_spoken][0] - spoken[last_spoken][1]

        speak(turn, round_number, spoken)
        last_spoken = round_number

        if turn == break_at:
            break
        turn += 1
    
    return last_spoken
   
if __name__ == '__main__':
    print("part1:",play(numbers.copy(), 2020))
    print("part2:",play(numbers.copy(), 30000000))
