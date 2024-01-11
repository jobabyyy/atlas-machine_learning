#!/usr/bin/env python3

import gym
import time

# init env
env = gym.make('Breakout-v0')

# reset state
state=env.reset()

for step in range(int(1e3)):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)

    print('reward: '+str(reward))
    print('done: '+str(done))
    
    time.sleep(0.1)
    
    if done:
        print('end reward: '+str(reward))
        
        break
    
        env.reset()

env.close()