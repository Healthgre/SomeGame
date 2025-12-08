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
    with patch("random.choice", return_value=data["enemy"][0]):
        enemy = load_enemy(str(temp_json))

    # === Получаем ожидаемые данные ===
    expected = data["enemy"][0]
    expected_weapon = expected["weapon"]
    expected_armor = expected["armor"]

    # Проверка оружие
    assert isinstance(enemy.weapon, EnemyWeapon)
    assert enemy.weapon.name == expected_weapon["name"]
    assert enemy.weapon.description == expected_weapon["description"]
    assert enemy.weapon.damage == expected_weapon["damage"]
    assert enemy.weapon.hit_chance == expected_weapon["hit_chance"]

    # Проверка броню
    assert isinstance(enemy.armor, EnemyArmor)
    assert enemy.armor.name == expected_armor["name"]
    assert enemy.armor.description == expected_armor["description"]
    assert enemy.armor.defense == expected_armor["defense"]

    # Проверка врага
    assert isinstance(enemy, Enemy)
    assert enemy.name == expected["name"]
    assert enemy.hp == expected["hp"]
    assert enemy.description == expected["description"]
    assert enemy.death_description == expected["death_description"]
