#!/usr/bin/env python3
"""
Q-Learning: Training
"""

import numpy as np


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1,
          gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):

    """
    function that performs Q-learning:

    env: is the FrozenLakeEnv instance
    Q: is a numpy.ndarray containing the Q-table
    episodes: is the total number of episodes to train over
    max_steps: is the maximum number of steps per episode
    alpha: is the learning rate
    gamma: is the discount rate
    epsilon: is the initial threshold for epsilon greedy
    min_epsilon: is the minimum value that epsilon
                 should decay to
    epsilon_decay: is the decay rate for updating epsilon
                   between episodes
    When the agent falls in a hole, the reward should be
    updated to be -1
        Returns: Q, total_rewards
                Q: is the updated Q-table
                total_rewards is a list containing the
                rewards per episode
    """
    # initialize Q-Values
    total_rewards = []
    for episode in range(episodes):
        # reset stage for each episode
        state = env.reset()
        done = False
        # tracking rewards within episode
        current_rewards = 0

        for step in range(max_steps):
            # Exploration-exploitation trade-off
            if np.random.uniform(0, 1) > epsilon:
                action = np.argmax(Q[state, :])
            else:
                action = env.action_space.sample()

            new_state, reward, done, info = env.step(action)

            # Update Q-table for Q(s,a)
            Q[state, action] = (
                Q[state, action
                 ] * (1 - alpha) + alpha * (reward + gamma * np.max(Q[new_state, :])))
            # set current state to new state
            state = new_state
            current_rewards += reward 

            if done == True:
                break

        # Exploration rate decay
        epsilon = min_epsilon + (epsilon - min_epsilon
                                 ) * np.exp(-epsilon_decay * episode)

        total_rewards.append(current_rewards)

    return Q, total_rewards
