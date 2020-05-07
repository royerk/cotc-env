from cotc_env.envs.cotc_env_easy import CotcEnvEasySolo


def test_cotc_easy_solo_step_no_crash():
    env = CotcEnvEasySolo()
    env.step(0)
    assert True
