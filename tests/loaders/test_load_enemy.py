import json
from unittest.mock import patch

from game.loader.enemyLoader import load_enemy
from game.enemy.enemy import Enemy
from game.enemy.enemyWeapon import EnemyWeapon
from game.enemy.enemyArmor import EnemyArmor


def test_load_enemy(json_path, tmp_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        # временный json
        temp_json = tmp_path / "enemy.json"
        # работает - НЕ СЛОМАЙ!!!
        temp_json.write_text(json.dumps(data, ensure_ascii=False), encoding="UTF-8")

        # мокнул рандомный выбор врага - надо читануть подучить.
        with patch("random.randint", return_value=0):
            enemy = load_enemy(str(temp_json))

        # проверяем оружие
        weapon_data = data["enemy"]["weapon"]
        assert isinstance(enemy.weapon, EnemyWeapon)
        assert enemy.weapon.name == weapon_data["name"]
        assert enemy.weapon.description == weapon_data["description"]
        assert enemy.weapon.damage == weapon_data["damage"]
        assert enemy.weapon.hit_chance == weapon_data["hit_chance"]

        # проверяем броню
        armor_data = data["enemy"]["armor"]
        assert isinstance(enemy.armor, EnemyArmor)
        assert enemy.armor.name == armor_data["name"]
        assert enemy.armor.description == armor_data["description"]
        assert enemy.armor.defense == armor_data["defense"]

        # проверяем самого врага
        assert isinstance(enemy, Enemy)
        assert enemy.hp == data["enemy"]["hp"]
        assert enemy.name == data["enemy"]["name"][0]
        assert enemy.description == data["enemy"]["description"][0]
        assert enemy.death_description == data["enemy"]["death_description"][0]
