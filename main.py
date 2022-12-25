"""

Reinforcement Learning Tic Tac Toe

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

    board = Environment()
    # board.printBoard()
    # board.playMove('X', (1, 1))
    # board.printBoard()

    agent = Agent()
    # print(agent.chooseRandomMove(board))

    # pp(agent.state_space)
    # pp(agent.action_space)

    # agent.printQTable()

    agent.selfPlay(num_episodes = 1, board = board)

    #TrainAgent(reps = 1)
    #TestAgent(reps = 1)

if __name__ == "__main__":
    main()



"""
Current progress:

i am working on tic tac toe with reinforcement learning. i am here:

ok the q table is working, now i need to

Loop through a number of episodes of self-play, during which the algorithm will explore the state space and update the Q-table. In each episode, the algorithm will:
To loop through a number of episodes of self-play, you can use a for loop. Here is an example of how you can do this:

Copy code
for episode in range(num_episodes):
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    # Initialize the player to be 'X'
    player = 'X'
    
    # Loop until the game is over or the board is full
    while not is_game_over(board) and not is_board_full(board):
        # Choose an action using the Q-table and the current state
        action = choose_action(board, q_table)
        # Update the board with the chosen action
        board = update_board(board, action, player)
        # Switch to the other player
        player = 'O' if player == 'X' else 'X'
    # Update the Q-table with the final reward for the episode
    update_q_table(board, q_table)
This code initializes the board and the player, and then enters a loop that continues until the game is over or the board is full. In each iteration of the loop, the algorithm chooses an action using the Q-table and the current state, updates the board with the chosen action, and switches to the other player. Once the game is over or the board is full, the Q-table is updated with the final reward for the episode.

You will need to define the following helper functions:

is_game_over(board): returns True if the game is over (i.e., someone has won or the board is full), and False otherwise.
is_board_full(board): returns True if the board is full (i.e., all positions are occupied), and False otherwise.
choose_action(board, q_table): chooses an action using the Q-table and the current state of the board.
update_board(board, action, player): updates the board with the given action and player.
update_q_table(board, q_table): updates the Q-table with the final reward for the episode.
 
i am currently on the update_q_table step. how do i do that?

"""

# also need to sanitize human input so we don't crash