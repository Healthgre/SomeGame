import json
import random
from pathlib import Path

from game.player.player import Player
from game.player.playerArmor import PlayerArmor
from game.player.playerWeapon import PlayerWeapon

path = Path(__file__).parent.parent / "json" / "data.json"


def loadPlayer(path: str):
    randPlayer = random.randint(0, 2)
    randDeath = random.randint(0, 1)

    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)

        player_data = data["player"]

        weapon_data = player_data["weapon"]
        armor_data = player_data["armor"]

        weapon = PlayerWeapon(
            weapon_data["name"],
            weapon_data["description"],
            weapon_data["damage"],
            weapon_data["hit_chance"]
        )

        armor = PlayerArmor(
            armor_data["name"],
            armor_data["description"],
            armor_data["defense"]
        )

        return Player(
            hp=player_data["hp"],
            description=player_data["description"][randPlayer],
            name=player_data["name"][randPlayer],
            weapon=weapon,
            armor=armor,
            death_description=player_data["death_description"][randDeath]
        )
