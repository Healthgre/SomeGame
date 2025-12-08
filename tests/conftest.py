from pathlib import Path

import pytest

from game.dungeon.dungeon import Dungeon
from game.dungeon.room import Room
from game.enemy.enemy import Enemy
from game.enemy.enemyArmor import EnemyArmor
from game.enemy.enemyWeapon import EnemyWeapon
from game.player.player import Player
from game.player.playerArmor import PlayerArmor
from game.player.playerWeapon import PlayerWeapon


@pytest.fixture
def json_path():
    return str(Path(__file__).parent.parent / "sources" / "game" / "json" / "data.json")


@pytest.fixture
def player_fixture():
    weapon = PlayerWeapon("test_name", "test_description", 5, 100)
    armor = PlayerArmor("test_name", "test_description", 3)

    return Player(
        hp=10,
        description="test_player",
        name="test_name",
        weapon=weapon,
        armor=armor,
        death_description="player is dead",
    )


@pytest.fixture
def enemy_fixture():
    weapon = EnemyWeapon("test_name", "test_description", 5, 100)
    armor = EnemyArmor("test_name", "test_description", 3)
    return Enemy(
        name="test_name",
        hp=8,
        description="test_enemy",
        death_description="enemy is dead",
        weapon=weapon,
        armor=armor
    )


@pytest.fixture
def dungeon_fixture():
    def make_enemy():
        return Enemy(
            name="test_name",
            hp=8,
            description="test_enemy",
            death_description="enemy is dead",
            weapon=EnemyWeapon("test_name", "test_description", 5, 100),
            armor=EnemyArmor("test_name", "test_description", 3)
        )

    rooms = [
        Room(0, "Start room", enemy=None, is_start_room=True, is_exit_room=False),
        Room(1, "Second room", enemy=make_enemy(), is_start_room=False, is_exit_room=False),
        Room(2, "Third room", enemy=None, is_start_room=False, is_exit_room=False),
        Room(3, "Forth room", enemy=make_enemy(), is_start_room=False, is_exit_room=False),
        Room(4, "Fifth room", enemy=None, is_start_room=False, is_exit_room=False),
        Room(5, "Sixth room", enemy=make_enemy(), is_start_room=False, is_exit_room=False),
        Room(6, "Exit room", enemy=None, is_start_room=False, is_exit_room=True),
    ]
    return Dungeon(rooms)
