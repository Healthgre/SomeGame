import pytest

from game.enemy.enemyWeapon import EnemyWeapon

@pytest.mark.enemy_weapon
def test_enemy_weapon_to_dict():
    weapon = EnemyWeapon("test_name", "test_description", 4, 80)
    data = weapon.to_dict()

    assert data["name"] == "test_name"
    assert data["description"] == "test_description"
    assert data["damage"] == 4
    assert data["hit_chance"] == 80
