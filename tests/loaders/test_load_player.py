import json
from unittest.mock import patch

from game.loader.playerLoader import load_player
from game.player.player import Player
from game.player.playerWeapon import PlayerWeapon
from game.player.playerArmor import PlayerArmor


def test_load_player(json_path, tmp_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        # создание временного json
        temp_json = tmp_path / "data.json"
        # работает - НЕ СЛОМАЙ!!!
        temp_json.write_text(json.dumps(data, ensure_ascii=False), encoding="UTF-8")

        # мокнул рандомный выбор данных по игроку - надо читануть подучить.
        with patch("random.randint", return_value=0):
            player = load_player(str(temp_json))

        weapon_data = data["player"]["weapon"]
        assert isinstance(player.weapon, PlayerWeapon)
        assert player.weapon.name == weapon_data["name"]
        assert player.weapon.description == weapon_data["description"]
        assert player.weapon.damage == weapon_data["damage"]
        assert player.weapon.hit_chance == weapon_data["hit_chance"]

        armor_data = data["player"]["armor"]
        assert isinstance(player.armor, PlayerArmor)
        assert player.armor.name == armor_data["name"]
        assert player.armor.description == armor_data["description"]
        assert player.armor.defense == armor_data["defense"]

        assert isinstance(player, Player)
        assert player.hp == data["player"]["hp"]
        assert player.name == data["player"]["name"][0]
        assert player.description == data["player"]["description"][0]
        assert player.death_description == data["player"]["death_description"][0]


