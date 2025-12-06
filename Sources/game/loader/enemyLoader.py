import json
import random
from pathlib import Path

from game.enemy.enemy import Enemy
from game.enemy.enemyArmor import EnemyArmor
from game.enemy.enemyWeapon import EnemyWeapon

path = Path(__file__).parent.parent / "json" / "data.json"


def load_enemy(path: str):
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)

        enemy_data = data["enemy"]

        random_enemy = random.choice(enemy_data)

        weapon_data = random_enemy["weapon"]
        weapon = EnemyWeapon(
            weapon_data["name"],
            weapon_data["description"],
            weapon_data["damage"],
            weapon_data["hit_chance"]
        )

        armor_data = random_enemy["armor"]
        armor = EnemyArmor(
            armor_data["name"],
            armor_data["description"],
            armor_data["defense"]

        )

        return Enemy(
            name=random_enemy["name"],
            hp=random_enemy["hp"],
            description=random_enemy["description"],
            death_description=random_enemy["death_description"],
            weapon=weapon,
            armor=armor

        )