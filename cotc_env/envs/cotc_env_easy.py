import gym
import time
from gym import spaces

from cotc_env.envs.state_solo import StateSolo
from cotc_env.envs.constants import *


class CotcEnvEasySolo(gym.Env):

    def __init__(self):
        self.state = StateSolo()
        self.action_space = spaces.Discrete(NUMBER_ACTIONS)
        self.observation_space = spaces.Dict({
            'self': spaces.Dict({
                'rum': spaces.Discrete(SHIP_MAX_RUM + 1),
                'x': spaces.Discrete(MAP_WIDTH),
                'y': spaces.Discrete(MAP_HEIGHT),
                'cap': spaces.Discrete(5),
                'speed': spaces.Discrete(3)
            }),
            'map': spaces.Box(-1, 2, shape=(MAP_WIDTH, MAP_HEIGHT), dtype=int)
        })

    def step(self, action):
        self.state.apply_action(action)
        return self.state.get_observation(), \
               self.state.get_reward(), \
               self.state.is_done(), \
               self.state.get_info()

    def reset(self):
        self.state = StateSolo()
        return self.state.get_observation()

    def render(self, mode='human'):
        self.state.show()

    def close(self):
        pass
