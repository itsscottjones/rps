import random
import constants
import functions.menu_functions as menu
import functions.logic_functions as logic
import functions.other_functions as other




def opponent_select():
    while True:
        opponent = input().lower().strip()
        if opponent in constants.ACTIVE_OPPONENTS:
            return opponent
        print("\nThat is not a valid game mode\n")
        menu.opponent_menu()


def get_valid_player_name():
    while True:
        player_name = input(": ").lower().strip()
        if other.is_player_name_valid(player_name):
            return player_name
        print("\nOnly letters, numbers, and spaces allowed\n")


def choose_rounds():
    while True:
        amount = input("Enter Rounds: ")

        if amount.isdigit():
            amount = int(amount)
            if amount in [1, 3, 5, 7, 9]:
                return amount
        print("\nThat is an invalid amount of rounds.\n")


def player_move_input():
    while True:
        player_move = input("Enter your move: ").lower().strip()

        if player_move == "r":
            player_move = "rock"
        elif player_move == "p":
            player_move = "paper"
        elif player_move == "s":
            player_move = "scissors"
        if player_move in constants.MOVES:
            return player_move
        
        print("That is not a valid input, try again..\n")


def get_computer_move():
    move = constants.COMPUTER_MOVES[random.randint(0, 2)]
    return move


def calculate_round_winner(p1_move, p2_move):
    if p1_move == p2_move:
        return 0, 0
        
    elif p1_move == "rock" and p2_move == "scissors" or \
            p1_move == "paper" and p2_move == "rock" or \
            p1_move == "scissors" and p2_move == "paper":
        return 1, 0
    
    else:
        return 0, 1   


def end_game_conditions(player1_total_score, player2_total_score, best_of):
     if player1_total_score == (best_of //2) + 1:
        return True
    
     elif player2_total_score == (best_of //2) + 1:
        return True

    #  print(player1_total_score, player2_total_score, player1_round_score, player2_round_score)