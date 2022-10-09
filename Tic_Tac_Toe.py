# This is a small python program that runs a two player game of chess.  
# This program does not require any sort of GUI.  It was written by
# William Elegy as a beginner level python project in 2022.
from IPython.display import clear_output
import random
    
    
def choose_first(player1,player2):
# The choose_first function randomly selects which player will go 
# first.  It displays the result as output and stores the result in the 
# first_player variable.
    
    first_player = random.randint(1,2)
                            
    if first_player == 1:
        print(f"{player1} is going first")

    else:
        print(f"{player2} is going first")



def display_board(board):
# The display_board function is used to display the playing board 
# to the players.  Individual indexes numbers are called from the board 
# list to show there values in their respective "cells" so that an X or 
# O will be shown if one has been placed in that "cell".  The "cell's" 
# number will be shown if the "cell" is free.

    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")


def place_marker(board, marker, position):
# The place_marker function takes in the board list and a position and 
# uses those to replace the value at the position's index in the board 
# list with the current player's marker.  It then returns the updated 
# board list.

    board[position] = marker
    return board


def space_check(board, position):
# The space_check function makes sure that the index at the board list 
# is not already an "X" or "O".  This is used before the place marker 
# function is run so that the program can ask the player for a valid 
# choice before it is applied to the board list.

    return board[position] != "X" and board[position] != "O"


def player_choice(board):
# The player_choice function asks the player which space they would 
# like to place their marker in.  It check to make sure they number is 
# valid and then uses the space_check function to make sure the space 
# is not already occupied by an "X" or "O".  Once the player gives an 
# input that passes all of the checks, it will return that position so 
# it can be used by place_marker.

    pos_list = ["1","2","3","4","5","6","7","8","9"]

    current_position = input("Please select a position 1-9: ")

    while current_position in pos_list:

        if space_check(board,int(current_position)) == False:
            current_position = input("That position is taken. "
                                     "Select a position 1-9: ")

        else:
            return int(current_position)

    while current_position not in pos_list:
        current_position = input("I don't understand. Select a position 1-9: ")

        while current_position in pos_list:

            if space_check(board,int(current_position)) == False:
                current_position = input("That position is taken. "
                                         "Select a position 1-9: ")

            else:
                return int(current_position)


def win_check(board, marker):
# The win_check function uses different patterns of indices in the 
# board list to check to see if the player has won.  If the player has 
# won, win_check will return True.  If the player has not won, 
# win_check will return False

    if board[1] == marker and board[4] == marker and board[7] == marker:
        return True

    elif board[2] == marker and board[5] == marker and board[8] == marker:
        return True

    elif board[3] == marker and board[6] == marker and board[9] == marker:
        return True

    elif board[1] == marker and board[2] == marker and board[3] == marker:
        return True

    elif board[4] == marker and board[5] == marker and board[6] == marker:
        return True

    elif board[7] == marker and board[8] == marker and board[9] == marker:
        return True

    elif board[1] == marker and board[5] == marker and board[9] == marker:
        return True

    elif board[3] == marker and board[5] == marker and board[7] == marker:
        return True

    else:
        return False


def tie_check(board):
# The tie_check function uses the space_check function to check if
# every value in the board list is either "X" or "O". It then uses the 
# win_check function to check if either player has won. If every use of 
# space_check and win_check returns False, tie_check will return True. 
# This means that there is a tie.  Otherwise, there was no tie and 
# tie_check will return False.

    if (space_check(board,1) == False
            and space_check(board,2) == False
            and space_check(board,3) == False
            and space_check(board,4) == False
            and space_check(board,5) == False
            and space_check(board,6) == False
            and space_check(board,7) == False
            and space_check(board,8) == False
            and space_check(board,9) == False
            and win_check(board,"X") == False
            and win_check(board,"O") == False):
        return True

    else:
        return False


def player_input(first_marker):
# The player_input function asks the player to choose their marker. The 
# function then makes sure that the player's input was actually "X" or 
# "O". If the input was not one of those, the function will continue to 
# ask the player for an input until it is either "X" or "O". Once the 
# input passes the checks, it will be returned.

    marker = "_"

    while marker.upper() not in ["X","O"]:
        marker = input("Please choose X or O: ")

        while marker.upper() not in ["X","O"]:
            marker = input("Sorry, I dont understand. Please choose X or O: ")

    if marker.upper() == "X":
        first_marker = "X"

    else:
        first_marker = "O"

    return first_marker


def replay_func():
# The replay_func function asks the player if they would like to play 
# again. The function will repeatedly ask for correct input until the 
# player inputs "Y" for yes or "N" for no. Once the input has passed 
# all of the checks, the function will either return play_again with 
# the value of "Y" if they entered "Y" or return nothing if the player 
# entered "N".

    play_again = "_"

    while play_again.upper() not in ["Y","N"]:
        play_again = input("Would you like to play again? (Y or N): ")

        while play_again.upper() not in ["Y","N"]:
            play_again = input("I dont understand. Please enter Y or N: ")

    return play_again == "Y"


def main():
# The main funtion is where all fo the previously built functions are 
# put to use.  This starts with replay set to True to get the game to 
# play one full round without asking the user if they would like to play.
    player1 = input("First player, what is your name? ")
    player2 = input("Second player, what is your name? ")
    replay = True

    # Begin the first round.  Select who will go first with 
    # choose_first.  Then, it will ask the first player if they want to 
    # be "X" or "O".
    while replay == True:
        first_marker = "_"
        second_marker = "_"
        board = ["$","1","2","3","4","5","6","7","8","9"]
        print("Welcome to tic tac toe!")
        choose_first(player1,player2)
        first_marker = player_input(first_marker)

        # Set the second player's marker to the opposite of the 
        # first player's marker.  Then, use clear_output to clear cell.
        if first_marker.upper() == "X":
            second_marker = "O"

        else:
            second_marker = "X"

        clear_output()

        # As long as no player has won and there has not been a tie, 
        # this while loop will continue to ask players to choose
        # spaces to place their markers in and then places those 
        # markers for the player.  Once a tie or win occurs the 
        # program will let the player know and break out of the loop.
        while (win_check(board,first_marker) == False
                and win_check(board,second_marker) == False
                and tie_check(board) == False):
            # The first player's turn begins.
            print(f"It is {first_marker}'s turn")
            # The board is displayed.
            display_board(board)
            # The player chooses a space.
            current_position = player_choice(board)
            # The player's marker is placed in the chosen space.
            place_marker(board,first_marker,current_position)
            clear_output()

            # Check for a tie and end the game if there is a tie.
            if tie_check(board) == True:
                display_board(board)
                print("The game has ended in a tie!")
                break

            # Check if the player has won and end the game if they have.
            elif win_check(board,first_marker) == True:
                display_board(board)
                print(f"{first_marker} has won!")
                break

            # The second player's turn begins.
            else:
                print(f"It is {second_marker}'s turn")
                # The board is displayed.
                display_board(board)
                # The player chooses a space.
                current_position = player_choice(board)
                # The player's marker is placed in the chosen space.
                place_marker(board,second_marker,current_position)
                clear_output()

                # Check for a tie and end the game if there is a tie.
                if tie_check(board) == True:
                    display_board(board)
                    print("The game has ended in a tie!")
                    break

                # Check if the player has won and end the game if they 
                # have.
                elif win_check(board,second_marker) == True:
                    display_board(board)
                    print(f"{second_marker} has won!")
                    break

                else:
                    pass

# The player will be asked if they would like to play again. If they 
# say yes, the program will restart and the beginning of the loop.  
# If they say no, the program will thank them for playing and close.
        replay = replay_func()
        clear_output()
        print("Thanks for playing!")


main()
