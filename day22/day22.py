"""
adventofcode 2020 day 22
"""

import copy
import pickle

def main():
    raw_players = open("day22/puzzle_input").read().split("\n\n")
    decks = dict()
    for player in raw_players:
        player, *cardlist = player.split("\n")
        decks[player[:-1]] = [int(c) for c in cardlist]

    # part 1
    win_player, win_deck = play_combat(copy.deepcopy(decks))
    score = sum(card * (index+1) for index, card in enumerate(reversed(win_deck)))
    print(f"part1: {win_player} wins with deck {win_deck}, score is {score}")

    # part 2, now with more rules
    win_player, win_deck = play_recursive_combat(copy.deepcopy(decks))
    score = sum(card * (index+1) for index, card in enumerate(reversed(win_deck)))
    print(f"part2: {win_player} wins with deck {win_deck}, score is {score}")

def play_combat(game_decks):
    iter_round = 1
    number_cards = sum(len(deck) for deck in game_decks.values())
    while True:
        current_round = dict()
        for player, deck in game_decks.items():
            current_round[player] = deck.pop(0)

        winner = [player for player, card in current_round.items() if card == max(current_round.values())][0]
        game_decks[winner].extend(sorted(current_round.values(), reverse=True))
        iter_round += 1
        game_winner = {player: deck for player, deck in game_decks.items() if len(deck) == number_cards}
        if len(game_winner) > 0:
            return next(iter(game_winner.items()))

def play_recursive_combat(game_decks, game_id = 1):
    round_id = 0
    played_states = set()
    number_cards = sum(len(deck) for deck in game_decks.values())
    while True:
        round_id += 1
        current_state = pickle.dumps(game_decks)
        if current_state in played_states:
            winner = "Player 1"
            return winner, game_decks[winner]

        played_states.add(current_state)
        current_round = dict()
        for player, deck in game_decks.items():
            current_round[player] = deck.pop(0)

        if all(len(game_decks[player]) >= card for player, card in current_round.items()):
            sub_decks = dict()
            for player, deck in game_decks.items():
                sub_decks[player] = deck[:current_round[player]]
            winner, _ = play_recursive_combat(sub_decks, game_id + 1)
            if winner == 'Player 1':
                append_deck = [current_round[winner], current_round['Player 2']]
            else:
                append_deck = [current_round[winner], current_round['Player 1']]
            game_decks[winner].extend(append_deck)
        else:
            winner = [player for player, card in current_round.items() if card == max(current_round.values())][0]
            game_decks[winner].extend(sorted(current_round.values(), reverse=True))

        game_winner = {player: deck for player, deck in game_decks.items() if len(deck) == number_cards}
        if len(game_winner) > 0:
            win_player, win_deck = next(iter(game_winner.items()))
            return win_player, win_deck

if __name__ == '__main__':
    main()
