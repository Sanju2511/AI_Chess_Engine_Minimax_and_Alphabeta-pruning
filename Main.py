from Board import DisplayBoard 
from MiniMax import minimax
from Evaluation import Evalualtion
import chess
import pygame as py

# Min Max evaluation Limits
MAX, MIN = 100000, -100000 # 100000 is the max value and -100000 is the min value
depth = 4 # Depth of the game tree

board = chess.Board() # Initialize the board
display = DisplayBoard(board) # Initialize the display

# Function to reset the game and return to the main menu
def setup_game():
    board.reset_board() # This resets the board to its initial state
    display.main_menu() # This shows the main menu of the game before starting
    display.update(board)
    run()

# Function to handle the user moves
def move():
    player_possible_move = display.square_select(py.mouse.get_pos()) # This gets the square the user has selected
    if player_possible_move != None:
        try:
            eval = Evalualtion(board, display.player_color) # This evaluates the move based on the current state of the board
            is_late_game = eval.is_late_game() # It checks if the game is in its late stage

            if display.player_color == "W":
                makeMoveWhite(player_possible_move, is_late_game) 
                makeMoveBlack(player_possible_move, is_late_game)
            else:
                makeMoveBlack(player_possible_move, is_late_game)
                makeMoveWhite(player_possible_move, is_late_game)
        except:
            print("Invalid Move")  # To find invalid move attempts

# Function to handle White's move and AI response
def makeMoveWhite(move, is_late_game):

    if display.player_color == "W": # If the player is white
        board.push_uci(move) # To Execute the player's move 
    else:
        # The depth attribute has to be odd
        if is_late_game:
            white = minimax(depth + 1, True, MIN, MAX, board, True) # Min Max move for late game
        else:
            white = minimax(depth + 1, True, MIN, MAX, board, True) # Min Max move if its not late game

        board.push(white) # To Execute the AI's move

    display.update(board) # To update the display with the new board state

# Function to handle Black's move and AI response
def makeMoveBlack(move, is_late_game):

    if display.player_color == "B": # If the player is black
        board.push_uci(move)
    else:
        # The depth attribute has to be even
        if is_late_game:
            black = minimax(depth + 2, False, MIN, MAX, board, True) # Min Max move for late game
        else:
            black = minimax(depth, False, MIN, MAX, board, True) # Min Max move if its not late game
        board.push(black)

    display.update(board)

#  TO Check if the game has ended
def is_game_over(board):
    if board.is_game_over():
        display.run = False # To stop the game loop
        display.game_over = True # To indicate that the game has ended
        display.game_over_menu() # To display the game over menu


def run(): # Main game loop
    if display.player_color == "B": # If the player is black
        makeMoveWhite(None, False) # To make the first move for white

    while display.run:
        events = py.event.get() # To get the user inputs from the display
        for event in events:
            if event.type == py.QUIT: # If the user closes the window
                exit()

            if event.type == py.MOUSEBUTTONDOWN and event.button == 1: # Left-click to move
                move()
            elif event.type == py.MOUSEBUTTONDOWN and event.button == 3: # Right-click to deselect
                display.remove_square_select()

        display.update_screen() # To update the display with the current board state
        is_game_over(board) # To check if the game has ended

while run: 
    setup_game()

py.quit()