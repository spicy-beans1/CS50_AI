"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # set counter for x and o
    x_count = 0
    o_count = 0

    # count how many xs and os are on the board
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    # if x==o it is x turn
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_set = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                empty_set.add((i,j))
    return empty_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    # if action is not valid return an error
    if board[i][j] is not EMPTY:
        raise Exception("Invalid Choice")

    #make a copy of the original board
    board_copy = copy.deepcopy(board)

    #retreive the move from the most recent move
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #loop though rows and columns to find a 3 in a row
    #if vertical
    for row in board:
        for j in range(0-2)
        if row==

    #horizontal
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
           
    #diagnal
    #assume 1 winner
    # if there is no winner return none


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #if X wins return 1
    # if O wins return -1
    # tie =0 
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
