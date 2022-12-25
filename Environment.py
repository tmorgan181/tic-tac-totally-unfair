"""

This script handles the implementation of the first reinforcement learning step:

1. Define the environment: Start by defining the environment in which the agent will operate.
    In this case, the environment will be a tic-tac-toe board.
    You'll need to decide how the board will be represented (e.g. as a 2D array or a list of lists),
    and how the agent will be able to interact with it (e.g. by choosing a square to place its symbol).

"""

from typing import Tuple, List
from pprint import pprint
import copy

class Environment:

    def __init__(self) -> None:
        
        # Initialize the board as a 2D array
        self.board = [[' ',' ',' '],
                      [' ',' ',' '],
                      [' ',' ',' ']]
        
        # Initialize the history of the board as a list of (state, action) pairs
        self.state_action_history = []

    def printBoard(self) -> None:
        
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

    def isGameOver(self) -> bool:
        
        # Check if board is full
        if self.isBoardFull():
            return True

        # Check if a player has won
        if self.checkWin() != '':
            return True

    def checkWin(self) -> str:

        board = self.board

        # Check rows
        for row in board:
            if row == ['X', 'X', 'X']:
                return 'X'
            elif row == ['O', 'O', 'O']:
                return 'O'
        
        # Check columns
        for col in range(3):
            if board[0][col] == 'X' and board[1][col] == 'X' and board[2][col] == 'X':
                return 'X'
            elif board[0][col] == 'O' and board[1][col] == 'O' and board[2][col] == 'O':
                return 'O'
        
        # Check diagonals
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return 'X'
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return 'O'
        if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            return 'X'
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            return 'O'
        
        # No player has won
        return ''

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
                
    def playMove(self, action: Tuple[int, int], symbol : str) -> None:
        
        # Check if invalid move
        if action not in self.availableActions():
            print("Not a valid action!")
            exit(1)

        if symbol != 'X' and symbol != 'O':
            print("Invalid symbol!")
            exit(1)

        # Place the symbol in the chosen square
        row = action[0]
        col = action[1]
        self.board[row][col] = symbol

        # Add the current state and action to the state-action history
        self.state_action_history.append((copy.deepcopy(self.board), action))

    def getStateActionHistory(self) -> List[Tuple[List[List[str]], Tuple[int, int]]]:
        return self.state_action_history