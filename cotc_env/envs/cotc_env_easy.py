import gym
from gym import error, spaces, utils
from gym.utils import seeding

from cotc_env.envs.state_solo import StateSolo
from cotc_env.envs.constants import *


class CotcEnvEasySolo(gym.Env):

    def __init__(self):
        self.state = None
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
        pass

    def reset(self):
        self.state = StateSolo()
        return self.state.get_observation()

    def render(self, mode='human'):
        pass

    def close(self):
        pass
