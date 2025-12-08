import pytest
from game.loader.dungeonLoader import load_dungeon
from game.dungeon.dungeon import Dungeon


@pytest.mark.dungeon
def test_load_dungeon(json_path):
    dungeon = load_dungeon(json_path)
    assert isinstance(dungeon, Dungeon)
    assert len(dungeon.rooms) == 7


@pytest.mark.dungeon
def test_first_is_created(json_path):
    dungeon = load_dungeon(json_path)
    start_room = dungeon.rooms[0]
    assert start_room.is_start_room is True


@pytest.mark.dungeon
def test_last_room_is_created(json_path):
    dungeon = load_dungeon(json_path)
    exit_room = dungeon.rooms[-1]
    assert exit_room.is_exit_room is True


@pytest.mark.dungeon
def test_enemy_rooms_are_created(json_path):
    dungeon = load_dungeon(json_path)
    enemy_rooms = [room for room in dungeon.rooms if room.enemy is not None]
    assert {room.number for room in enemy_rooms} == {1, 3, 5}
    assert len(enemy_rooms) == 3

# Тут проверяется стартовая и финишная комната, поэтому их не надо проверять отдельно от двух промежуточных
@pytest.mark.dungeon
def test_empty_rooms_are_created(json_path):
    dungeon = load_dungeon(json_path)
    empty_rooms = [room for room in dungeon.rooms if room.enemy is None]
    assert {room.number for room in empty_rooms} == {0, 2, 4, 6}
    assert len(empty_rooms) == 4


@pytest.mark.dungeon
def test_room_descriptions_is_working(json_path):
    dungeon = load_dungeon(json_path)
    for room in dungeon.rooms:
        assert isinstance(room.description, str)
        assert room.description.strip() != ""

