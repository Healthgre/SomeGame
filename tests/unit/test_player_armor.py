import pytest

from game.player.playerArmor import PlayerArmor


@pytest.mark.player_armor
def test_player_armor_to_dict():
    armor = PlayerArmor("test_armor", "test_description", 3)
    data = armor.to_dict()

    assert data["name"] == "test_armor"
    assert data["description"] == "test_description"
    assert data["defense"] == 3
