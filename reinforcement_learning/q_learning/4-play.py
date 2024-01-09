#!/usr/bin/env python3
"""Q-Learning:
Agent to perform an episode."""


import numpy as np
import gym


def play(env, Q, max_steps=100):
    """Function Play that has the trained
     agent play an episode.

    env: is the FrozenLakeEnv instance
    Q is a numpy.ndarray containing the Q-table
    max_steps: is the maximum number of
               steps in the episode

    Each state of the board should be displayed via the console
    You should always exploit the Q-table

    Returns: the total rewards for the episode
    """
    # awards player starts with
    total_rewards = 0
    # current state
    state = env.reset()


    for step in range(max_steps):
      # display current state
      env.render()

      # action chosen using qtable
      action = np.argmax(Q[state, :])

      # next action taken
      new_state, reward, done, info  = env.step(action)
      # update total rewards
      total_rewards += reward

      # next state
      state = new_state

      # checking if complete
      if done:
        break

    # close envirnoment
    env.close()

    return total_rewards

def main():
    load_frozen_lake = __import__('0-load_env').load_frozen_lake
    q_init = __import__('1-q_init').q_init
    train = __import__('3-q_learning').train
    play = __import__('4-play').play
    np.random.seed(0)
    desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
    env = gym.make("FrozenLake-v1", desc=desc, render_mode='human')
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    Q, total_rewards = train(env, Q)
    print(play(env, Q))

if __name__ == '__main__':
    main()