# import random
# import classes
import constants
import functions.menu_functions as menu
import functions.logic_functions as logic
import functions.print_scores_functions as print_scores
import functions.other_functions as other


def run_game():
    menu.welcome_message()
    while True:# logic.round_score_counter(player1_round_score, player2_round_score, player1_total_score, player2_total_score, player1, player2)
        menu.opponent_menu()
        opponent = logic.opponent_select()

        menu.choose_rounds()
        best_of = logic.choose_rounds()
        total_rounds = best_of

        player1_round_score, player2_round_score = constants.STARTING_SCORES, constants.STARTING_SCORES
        player1_total_score, player2_total_score = constants.STARTING_SCORES, constants.STARTING_SCORES


        if opponent == "p":
            menu.player1_name_input_menu()
            player1 = logic.get_valid_player_name()

            menu.player2_name_input_menu()
            player2 = logic.get_valid_player_name()

        elif opponent == "g":
            menu.player1_name_input_menu()
            player1 = logic.get_valid_player_name()
            player2 = constants.COMPUTER_NAME["g"]

        print(" ")

        while total_rounds >= 1:
            # if player1_round_score != 0 and player2_round_score != 0:
            # print(total_rounds)
            
            print(f'---ROUND START---\nBest of {best_of}.\nRounds Remaining: {total_rounds}')
            
            
            menu.player_move_menu()
            player1_move = logic.player_move_input()
            if opponent == "p":
                    player2_move = logic.player_move_input()
            elif opponent == "g":
                    player2_move = logic.get_computer_move()
            
            
            player1_round_score, player2_round_score = logic.calculate_round_winner(player1_move, player2_move)
            if player1_round_score != player2_round_score:
                 total_rounds -= 1
        
            player1_total_score += player1_round_score
            player2_total_score += player2_round_score

            print_scores.announce_total_wins(player1, player2, player1_total_score, player2_total_score)
            print_scores.announce_round_winner(player1_move, player2_move, player1, player2)



            if logic.end_game_conditions(player1_total_score, player2_total_score, best_of):
                 if player1_total_score > player2_total_score:
                      winner = other.name_cap(player1)
                 else:
                      winner = other.name_cap(player2)
                 print(f'---WE HAVE A WINNER---\n\n---FINAL SCORES---')
                 print(
                      f'{other.name_cap(player1)}: {player1_total_score}\n'
                      f'{other.name_cap(player2)}: {player2_total_score}')
                 print(f'Well Done {winner}!\n')
                 break
            #create scores files




run_game()

# # if pvc player1 = input name
# player1 = logic.get_valid_player_name("")
# # if pvp player1 = input name, player 2 = input name
# player1 = logic.get_valid_player_name("Player 1:")
# print(" ")
# player1 = logic.get_valid_player_name("Player 2: ")

# play game
# keep round score
# track round wins/ loses
# track game wins/ loses
# trackp hands wins, ties, losses - in order
