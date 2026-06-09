import random
import classes
import functions.menu_functions as menu_functions
from functions.menu_functions import name_cap
from constants import MOVES, COMPUTER_MOVES


# moves [rock, paper, sisscors]
# print before input [ROCK = R, PAPER = P, SCISSORS = S, Q = QUIT]
# input.lower# if P chooses rock and C chooses sissors
# elif P chooses paper and C chooses sissors
# elif P chooses scissors and C chooses paper
# You Win
# ELse You lose

# players = functions.choose_players()
# running = True
# When player chooses to quit "running = False"



# while running:
#     if players == "p":
#         functions.player_vs_player()
#     else:
#         functions.player_vs_com()   
#     pass


def keep_score(player1_total, player2_total, player1_score, player2_score):
     if total_rounds == starting_rounds:
         player1_total, player2_total = 0, 0
     player1_total += player1_score
     player2_total += player2_score
     print(f'{name_cap(player1)} wins: {player1_total}')
     print(f'{name_cap(player2)} wins: {player2_total}')
     return player1_total, player2_total


def end_game():
     if player1_total == (starting_rounds //2) + 1:
        print(f' \nCONGRATULATIONS, you beat {name_cap(player2)}')
        print(f'Best of {starting_rounds}: Scores {name_cap(player1)}: {player1_total} - {name_cap(player2)}: {player2_total}\n ')
        return True
    
     elif player2_total == (starting_rounds //2) + 1:
         print(f' \n{player2} handed you a beat down..')
         print(f'Best of {starting_rounds}: Scores {name_cap(player1)}: {player1_total} - {name_cap(player2)}: {player2_total}\n ')
         
         if player2 == "GLaDOS":
            print(f'You should probably quit. If you continue to bore {player2} she may get mad..\n ')
            return True
         else:
            print(" ")
            return True

