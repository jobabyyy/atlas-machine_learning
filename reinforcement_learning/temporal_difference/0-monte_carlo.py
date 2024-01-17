#!/usr/bin/env python3
""" Temporal Difference:
    Monte Carlo
"""


import numpy as np


def monte_carlo(env, V, policy, episodes=5000,
                max_steps=100, alpha=0.1, gamma=0.99):
    """
    function that performs the Monte Carlo Algorithm
    - env: is the openAI environment instance
    - V: is a numpy.ndarray of shape (s,)
         containing the value estimate
    - policy: is a function that takes in a state
              and returns the next action to take
    - episodes: is the total number of episodes
                to train over
    - max_steps: is the maximum number of steps
                 per episode
    - alpha: is the learning rate
    - gamma: is the discount rate
    Returns: V, the updated value estimate
    """
    # init v w/ zeros for all the states
    V = np.zeros(env.nS)

    # init empty list to store trajectory
    trajectory = []

    # init environment state
    state = env.reset()

    # select action based on current state
    action = policy(state)

    # observe next state and reward
    next_state, reward, done, = env.step(action)

    # append to trajectory list
    trajectory.append((state, action, reward))

    # update current state to next state
    state = next_state