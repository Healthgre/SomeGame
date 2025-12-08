import pytest
from game.controller.controller import game_loop
from game.dungeon.dungeon import Dungeon
from game.dungeon.room import Room
from game.player.player import Player
from game.player.playerWeapon import PlayerWeapon
from game.player.playerArmor import PlayerArmor
from game.enemy.enemy import Enemy
from game.enemy.enemyWeapon import EnemyWeapon
from game.enemy.enemyArmor import EnemyArmor


@pytest.mark.controller
def test_game_loop_exit_if_player_select_exit_from_last_room(monkeypatch, capfd):
    exit_room = Room(number=0, description="Exit room", is_exit_room=True)
    dungeon = Dungeon(rooms=[exit_room])

    player = Player(
        hp=10,
        description="test_description",
        name="test_name",
        weapon=PlayerWeapon("test_weapon", "test_description", damage=5, hit_chance=100),
        armor=PlayerArmor("test_armor", "test_description", defense=0),
        death_description="test_description"
    )

    # Почитать, доразобраться
    monkeypatch.setattr("builtins.input", lambda _: "3")

    game_loop(player, dungeon)
    # Почитать, доразобраться
    out, _ = capfd.readouterr()
    assert "Вы покинули подземелье." in out or "Вы нашли выход из подземелья!" in out


@pytest.mark.controller
def test_game_loop_exit_after_battle_and_exiting_out(monkeypatch, capfd):
    enemy = Enemy(
        name="test_enemy_name",
        hp=5,
        description="test_enemy_description",
        death_description="test_hero_enemy_death",
        weapon=EnemyWeapon("test_enemy_weapon_namee", "test_enemy_description_weapon", damage=1, hit_chance=0),
        armor=EnemyArmor("test_enemy_armor_name", "test_enemy_description_armor", defense=0)
    )
    enemy_room = Room(number=1, description="Enemy room", enemy=enemy)
    dungeon = Dungeon(rooms=[enemy_room])

    player = Player(
        hp=10,
        description="test_hero_description",
        name="test_hero_name",
        weapon=PlayerWeapon("test_hero_weapon_name", "test_hero_description_weapon", damage=5, hit_chance=100),
        armor=PlayerArmor("test_hero_armor_name", "test_hero_description_armor", defense=0),
        death_description="test_hero_description_death",
    )

    # Тут атакуем, а потом выходим, если забыть выйти то бесконечный цикл получается)))
    inputs = iter(["1", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game_loop(player, dungeon)
    out, _ = capfd.readouterr()
    assert "Вы вступили в бой!" in out
    assert "Вы покинули подземелье." in out or "Вы нашли выход из подземелья!" in out

    """Надо бы дописать тест про смерть героя в битве, про переходы назат, про уйти назад/вперёд из комнаты с врагом"""
