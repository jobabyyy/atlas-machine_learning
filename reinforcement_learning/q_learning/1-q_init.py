#!/usr/bin/env python3
"""
Q-Learning: Initialize Q-table
"""


import numpy as np


def q_init(env):
    # Get the number of states and actions from the environment
    num_states = env.observation_space.n
    num_actions = env.action_space.n
    
    # Initialize the Q-table with zeros
    q_table = np.zeros((num_states, num_actions))
    
    return q_table
