import pytest

from game.enemy.enemyArmor import EnemyArmor


@pytest.mark.enemy_armor
def test_enemy_armor_to_dict():
    armor = EnemyArmor("test_name", "test_description", 3)
    data = armor.to_dict()

    assert data["name"] == "test_name"
    assert data["description"] == "test_description"
    assert data["defense"] == 3
