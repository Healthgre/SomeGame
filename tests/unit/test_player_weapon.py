import pytest

from game.player.playerWeapon import PlayerWeapon


@pytest.mark.player_weapon
def test_player_weapon_to_dict():
    weapon = PlayerWeapon("test_weapon", "test_description", 5, 100)
    data = weapon.to_dict()

    assert data["name"] == "test_weapon"
    assert data["description"] == "test_description"
    assert data["damage"] == 5
    assert data["hit_chance"] == 100
