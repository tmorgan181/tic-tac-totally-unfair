"""
Author: Trenton Morgan
Date: 24-Dec-2022

Reinforcement Learning Tic Tac Toe

This script handles the driver function to execute the following reinforcement
learning steps:

1. Define the environment: Start by defining the environment in which the agent will operate.
    In this case, the environment will be a tic-tac-toe board.
    You'll need to decide how the board will be represented (e.g. as a 2D array or a list of lists),
    and how the agent will be able to interact with it (e.g. by choosing a square to place its symbol).

2. Define the agent: Next, you'll need to define the agent that will play the game.
    This will involve creating a class or function that implements the logic for choosing a move.
    You can start by having the agent choose moves randomly, and then gradually improve
    its performance by reinforcing good moves and penalizing bad ones.

3. Implement the reinforcement learning algorithm: There are many different algorithms you can use for
    reinforcement learning, such as Q-learning or SARSA. Choose one that you think will work well
    for the tic-tac-toe problem, and implement it in your program.

4. Train the agent: To train the agent, you'll need to play many games of tic-tac-toe against it,
    reinforcing good moves and penalizing bad ones. As the agent plays more games,
    it should gradually improve its performance.

5. Test the agent: Once you've trained the agent, you can test its performance by playing additional
    games against it. You can also try playing the agent as the first player to see how it performs in that role.

"""

from Environment import Environment
from Agent import Agent

def main():

    # board = Environment()
    # board.printBoard()
    # board.playMove('X', (1, 1))
    # board.printBoard()

    agent = Agent(learning_rate = 0.1, exploration_rate = 0.01)
    # print(agent.chooseRandomMove(board))

    # pp(agent.state_space)
    # pp(agent.action_space)

    # agent.printQTable()

    agent.selfPlay(num_episodes = 10000, agent_symbol = 'X')
    agent.playHuman(agent_symbol = 'X')

    #TrainAgent(reps = 1)
    #TestAgent(reps = 1)

if __name__ == "__main__":
    main()