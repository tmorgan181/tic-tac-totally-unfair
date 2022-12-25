"""

2. Define the agent: Next, you'll need to define the agent that will play the game.
    This will involve creating a class or function that implements the logic for choosing a move.
    You can start by having the agent choose moves randomly, and then gradually improve
    its performance by reinforcing good moves and penalizing bad ones.


"""

import random
from typing import Dict, Tuple, List
from collections import defaultdict
from pprint import pprint as pp

from Environment import Environment

class Agent:

    def __init__(self):

        self.state_space: List[Tuple[Tuple[str]]] = self.getStateSpace()
        self.action_space: List[Tuple[int, int]] = self.getActionSpace()
        self.q_table: Dict[Tuple[Tuple[str]], Dict[Tuple[int, int], float]] = self.initQTable()

    def chooseRandomMove(self, board: Tuple[Tuple[str]]) -> Tuple[int, int]:
        # Choose a random row and column index
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return (row, col)

    def getStateSpace(self) -> List[Tuple[Tuple[str]]]:
        # The state space consists of all possible configurations of the 2D List
        # For example, the following board configuration:
        # [['X', 'O', 'X'],
        #  [' ', 'X', 'O'],
        #  ['O', ' ', 'X']]
        # could be one element of the state space
        state_space = []
        # Generate all possible combinations of X, O, and ' '
        for i in ('X', 'O', ' '):
            for j in ('X', 'O', ' '):
                for k in ('X', 'O', ' '):
                    for l in ('X', 'O', ' '):
                        for m in ('X', 'O', ' '):
                            for n in ('X', 'O', ' '):
                                for o in ('X', 'O', ' '):
                                    for p in ('X', 'O', ' '):
                                        for q in ('X', 'O', ' '):
                                            # Only include valid configurations of the board in the state space
                                            if (i != ' ' and i == j and j == k) or\
                                                    (l != ' ' and l == m and m == n) or\
                                                    (o != ' ' and o == p and p == q) or\
                                                    (i != ' ' and i == l and l == o) or\
                                                    (j != ' ' and j == m and m == p) or\
                                                    (k != ' ' and k == n and n == q) or\
                                                    (i != ' ' and i == m and m == q) or\
                                                    (k != ' ' and k == m and m == o):
                                                state_space.append(((i, j, k), (l, m, n), (o, p, q)))
        return state_space

    def getActionSpace(self) -> List[Tuple[int, int]]:
        # The action space consists of all possible moves that can be made on the board
        # For example, the move (0, 1) would represent placing an X or O in the top middle cell of the board
        action_space = [(i, j) for i in range(3) for j in range(3)]
        return action_space

    def initQTable(self) -> Dict[Tuple[Tuple[str]], Dict[Tuple[int, int], float]]:
        q_table = defaultdict(lambda: {})
        for state in self.state_space:
            for i in range(3):
                for j in range(3):
                    q_table[state][(i, j)] = 0.0
        return q_table

    def printQTable(self):
        for state, actions in self.q_table.items():
            print(f"State: {state}")
            for action, value in actions.items():
                print(f"  Action: {action} Value: {value:.2f}")

    def chooseQTableAction(self, board: Environment, epsilon: float) -> Tuple[int, int]:
        # Convert the board to a tuple to use as a key in the Q-table
        state = tuple(tuple(row) for row in board.board)

        # If a random number is less than epsilon, explore a random action
        if random.random() < epsilon:
            return random.choice(board.availableActions())

        # Otherwise, exploit the best known action
        else:
            # Find the actions with the highest expected reward
            best_actions = []
            max_reward = -float('inf')
            for action, reward in self.q_table[state].items():
                if reward > max_reward:
                    best_actions = [action]
                    max_reward = reward
                elif reward == max_reward:
                    best_actions.append(action)

            # Choose a random action from the best actions
            if not best_actions:
                return random.choice(board.availableActions())
            else:
                return random.choice(best_actions)

    def updateQTable(self, board: Environment):
        print("* congrats!")

    def selfPlay(self, num_episodes: int, board: Environment):
        for episode in range(num_episodes):
            # Initialize the player to be 'X'
            player = 'X'
            
            # Loop until the game is over or the board is full
            while not board.isGameOver():
                # Choose an action using the Q-table and the current state
                action = self.chooseQTableAction(board, epsilon = 0.1)
                # Update the board with the chosen action
                board.playMove(action, player)
                board.printBoard()
                # Get human input for 'O'
                action = board.getHumanInput()
                board.playMove(action, 'O')
                board.printBoard()
                
            # Update the Q-table with the final reward for the episode
            self.updateQTable(board)




"""
Define the state space and action space for the game. The state space will consist of all possible configurations of the tic-tac-toe board, and the action space will consist of all possible moves that can be made in the game.

Initialize a Q-table with the same dimensions as the state space. The Q-table will store the expected reward for each action taken from each state.

Loop through a number of episodes of self-play, during which the algorithm will explore the state space and update the Q-table. In each episode, the algorithm will:

Select a starting state and an initial action according to some exploration strategy (e.g. epsilon-greedy).
Take the action and transition to the next state.
Update the Q-table based on the reward received and the expected reward of the next state (using the bellman equation).
Repeat the above steps until the episode terminates (e.g. when the game is won or drawn).
After training is complete, the Q-table will contain the expected reward for each action taken from each state. To choose the best action for a given state, the algorithm can simply select the action with the highest expected reward.
"""