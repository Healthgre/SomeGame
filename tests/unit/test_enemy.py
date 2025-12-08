def test_enemy_is_alive(enemy_fixture):
    assert enemy_fixture.is_alive() is True

    enemy_fixture.hp = 0
    assert enemy_fixture.is_alive() is False

    enemy_fixture.hp = 8
    enemy_fixture.take_damage(100)
    assert enemy_fixture.is_alive() is False


def test_enemy_take_damage(enemy_fixture):
    # броня = 3, урон = 10 - 3 проходится 7
    damage = enemy_fixture.take_damage(10)
    assert damage == 7
    assert enemy_fixture.hp == 1
