import gym
from gym import error, spaces, utils
from gym.utils import seeding

from cotc_env.envs.StateSolo import StateSolo


class CotcEnvEasySolo(gym.Env):

    def __init__(self):
        self.state = None

    def step(self, action):
        pass

    def reset(self):
        self.state = StateSolo()

    def render(self, mode='human'):
        pass

    def close(self):
        pass
