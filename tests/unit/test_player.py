import pytest


@pytest.mark.player
def test_player_is_alive(player_fixture):
    assert player_fixture.is_alive() is True

    player_fixture.hp = 0
    assert player_fixture.is_alive() is False

    player_fixture.hp = 10
    player_fixture.take_damage(100)
    assert player_fixture.is_alive() is False


@pytest.mark.player
def test_player_take_damage(player_fixture):
    # броня = 3, урон = 10, 10 - 3 = приходится 7

    damage = player_fixture.take_damage(10)
    assert damage == 7
    assert player_fixture.hp == 3
