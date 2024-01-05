#!/usr/bin/env python3
"""
Q-learning: Epsilon Greedy
"""


import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """
    function that uses epsilon-greedy to
    determine the next action:

    Q: is a numpy.ndarray containing the q-table
    state: is the current state
    epsilon: is the epsilon to use for the calculation
    Returns: the next action index
    """
    # random decision to determine if to explore or to exploit
    if np.random.uniform(1, 0) > epsilon:
        # explore
        action = np.random.randint(Q.shape[1])
    else:
        # exploit
        action = np.argmax(Q[state])

    return action
