from gym.envs.registration import register

register(
    id='cotc-v0',
    entry_point='cotc_env.envs:CotcEnvEasy',
)
# register(
#     id='foo-extrahard-v0',
#     entry_point='gym_foo.envs:FooExtraHardEnv',
# )