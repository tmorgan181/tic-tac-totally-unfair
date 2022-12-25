"""

This script handles the second and third steps:

2. Define the agent: Next, you'll need to define the agent that will play the game.
    This will involve creating a class or function that implements the logic for choosing a move.
    You can start by having the agent choose moves randomly, and then gradually improve
    its performance by reinforcing good moves and penalizing bad ones.

3. Implement the reinforcement learning algorithm: There are many different algorithms you can use for
    reinforcement learning, such as Q-learning or SARSA. Choose one that you think will work well
    for the tic-tac-toe problem, and implement it in your program.

"""

import random
from typing import Dict, Tuple, List
from collections import defaultdict
from pprint import pprint as pp

from Environment import Environment

class Agent:

    def __init__(self, learning_rate: float, exploration_rate: float) -> None:

        self.state_space: List[Tuple[Tuple[str]]] = self.getStateSpace()
        self.action_space: List[Tuple[int, int]] = self.getActionSpace()
        self.q_table: Dict[Tuple[Tuple[str]], Dict[Tuple[int, int], float]] = self.initQTable()
        self.learning_rate: float = learning_rate
        self.epsilon: float = exploration_rate

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

    def printQTable(self) -> None:
        
        for state, actions in self.q_table.items():
            print(f"State: {state}")
            for action, value in actions.items():
                print(f"  Action: {action} Value: {value:.2f}")

    def chooseQTableAction(self, board: Environment) -> Tuple[int, int]:
        
        # Convert the board to a tuple to use as a key in the Q-table
        state = tuple(tuple(row) for row in board.board)

        # If a random number is less than epsilon, explore a random action
        if random.random() < self.epsilon:
            return random.choice(board.availableActions())

        # Otherwise, exploit the best known action
        else:
            
            # Find the actions with the highest expected reward
            best_actions = []
            max_reward = -float('inf')
            for action, reward in self.q_table[state].items():
                if action not in board.availableActions():
                    continue
                if reward > max_reward:
                    best_actions = [action]
                    max_reward = reward
                elif reward == max_reward:
                    best_actions.append(action)

            # Choose a random action from the best actions, or a random valid action if no best actions are found
            if not best_actions:
                return random.choice(board.availableActions())
            else:
                return random.choice(best_actions)

    def selfPlay(self, num_episodes: int, agent_symbol: str) -> None:
        
        # Play 'num_episodes' number of games
        for episode in range(num_episodes):

            # Create a new environment for every game
            board = Environment()

            # Loop until the game is over or the board is full
            # In this loop a single move is played for a single player
            # Each time the loop iterates, the player changes
            # The agent plays against itself until game over
            # Each game begins with 'X' making the first move
            symbol = 'X'
            while not board.isGameOver():
                
                # Choose an action using the Q-table and the current state
                action = self.chooseQTableAction(board)
                
                # Update the board with the chosen action
                board.playMove(action, symbol)
                # board.printBoard()

                if symbol == 'X':
                    symbol = 'O'
                else:
                    symbol = 'X'

            # Determine the winner and update the Q-table with the final reward for the episode
            print("-----GAME OVER!-----")
            if board.checkWin() == '':
                print("It's a draw!")
                self.updateQTable(board, final_reward = 0.5)
            elif board.checkWin() == 'X' == agent_symbol:
                print("Agent wins with X!")
                self.updateQTable(board, final_reward = 1.0)
            elif board.checkWin() == 'O' == agent_symbol:
                print("Agent wins with O!")
                self.updateQTable(board, final_reward = 1.0)
            else:
                print("Agent loses.")
                self.updateQTable(board, final_reward = -1.0)

    def updateQTable(self, board: Environment, final_reward: float) -> None:

        history = board.getStateActionHistory()

        # Loop through the state-action history in reverse
        for i in range(len(history) - 1, -1, -1):
            
            state, action = history[i]

            # Convert the state to a tuple of tuples (able to be used as dict key)
            state = tuple(tuple(row) for row in state)
            print(state)
            print(action)

            # Get the current Q-value for this state-action pair
            current_q_value = self.q_table[state][action]
            print("Current: ", current_q_value)

            # Calculate the new Q-value using the Q-learning update rule
            # Q(s, a) = Q(s, a) + alpha * (reward - Q(s, a))
            new_q_value = current_q_value + self.learning_rate * (final_reward - current_q_value)
            print("New: ", new_q_value)

            # Update the Q-table with the new Q-value
            self.q_table[state][action] = new_q_value

    def playHuman(self, agent_symbol: str):

        # Create a new environment for every game
        board = Environment()

        # Loop until the game is over or the board is full
        # In this loop a single move is played for a single player
        # Each time the loop iterates, the player changes
        # The agent plays against a human giving input
        # Each game begins with 'X' making the first move
        symbol = 'X'
        while not board.isGameOver():
            action = ()

            # If it's the agent's turn
            if symbol == agent_symbol:
                # Choose an action using the Q-table and the current state
                action = self.chooseQTableAction(board)
            
            # Else it's the human's turn
            else:
                action = board.getHumanInput()

            # Update the board with the chosen action
            board.playMove(action, symbol)
            board.printBoard()

            if symbol == 'X':
                symbol = 'O'
            else:
                symbol = 'X'

        # Determine the winner and update the Q-table with the final reward for the episode
        print("-----GAME OVER!-----")
        if board.checkWin() == '':
            print("It's a draw!")
            self.updateQTable(board, final_reward = 0.5)
        elif board.checkWin() == 'X' == agent_symbol:
            print("Agent wins with X!")
            self.updateQTable(board, final_reward = 1.0)
        elif board.checkWin() == 'O' == agent_symbol:
            print("Agent wins with O!")
            self.updateQTable(board, final_reward = 1.0)
        else:
            print("Agent loses.")
            self.updateQTable(board, final_reward = -1.0)