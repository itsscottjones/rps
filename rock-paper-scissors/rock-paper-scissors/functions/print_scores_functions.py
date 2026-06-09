import random
import constants
import functions.menu_functions as menu
import functions.logic_functions as logic
import functions.other_functions as other




def announce_round_winner(p1_move, p2_move, player1, player2):
    player1_cap, player2_cap = other.name_cap(player1), other.name_cap(player2)
    if p1_move == p2_move:
        print(f'\nIt is a tie {p1_move.upper()} & {p2_move.upper()} are an equal match\n')
    
    elif p1_move == "rock" and p2_move == "scissors" or \
            p1_move == "paper" and p2_move == "rock" or \
            p1_move == "scissors" and p2_move == "paper":
        print(f'\n{player1_cap} wins! {p1_move.upper()} beats {p2_move.upper()}\n')

    else:
        print(f'\n{player2_cap} wins! {p2_move.upper()} beats {p1_move.upper()}\n')


def announce_total_wins(player1, player2, player1_total_score, player2_total_score):
    player1_cap, player2_cap = other.name_cap(player1), other.name_cap(player2)
    print(f'\n{player1_cap} total wins: {player1_total_score}')
    print(f'{player2_cap} total wins: {player2_total_score}')