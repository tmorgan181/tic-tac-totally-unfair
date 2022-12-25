"""

1. Define the environment: Start by defining the environment in which the agent will operate.
    In this case, the environment will be a tic-tac-toe board.
    You'll need to decide how the board will be represented (e.g. as a 2D array or a list of lists),
    and how the agent will be able to interact with it (e.g. by choosing a square to place its symbol).

"""

from typing import Tuple, List
from pprint import pprint

class Environment:

    def __init__(self):
        # Initialize the board as a 2D array
        self.board = [[' ',' ',' '],
                      [' ',' ',' '],
                      [' ',' ',' ']]

    def printBoard(self):
        # Output the current state of the board
        for i, row in enumerate(self.board):
            print('|'.join(row))

            if i < len(self.board) - 1:
                print('-' * 5)

        print('*' * 10)

    def isBoardFull(self) -> bool:
        for row in self.board:
            for space in row:
                if space == ' ':
                    return False
        return True

    def isGameOver(self):
        # Check if board is full
        if self.isBoardFull():
            return True

        board = self.board
        # Check if a player has won
        for i in range(3):
            # Check rows
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
                return True
            # Check columns
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
                return True
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return True

    def availableActions(self) -> List[Tuple[int, int]]:
        actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    actions.append((i, j))
        return actions

    def getHumanInput(self) -> Tuple[int, int]:
        # Get a valid action from human input
        valid = False
        while not valid:
            row = int(input("Give the row: "))
            col = int(input("And the col: "))
                
                if (row, col) in self.availableActions():
                    return(row, col)

            print("Invalid move.")
                
    def playMove(self, action: Tuple[int, int], symbol : str):
        # Place the symbol in the chosen square
        row = action[0]
        col = action[1]
        self.board[row][col] = symbol
