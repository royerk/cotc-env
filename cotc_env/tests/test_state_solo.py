from cotc_env.envs.state_solo import StateSolo


def test_apply_order_no_crash():
    state = StateSolo()
    state.apply_action(0)
    assert True
