import pytest
from game.dungeon.dungeon import Dungeon
from game.dungeon.room import Room


@pytest.mark.dungeon
def test_create_dungeon():
    rooms = [
        Room(0, "start", is_start_room=True),
        Room(1, "middle"),
        Room(2, "exit", is_exit_room=True)
    ]

    dungeon = Dungeon(rooms)

    assert dungeon.rooms == rooms
    assert dungeon.position == 0
    assert dungeon.current_room() is rooms[0]


@pytest.mark.dungeon
def test_move_forward_success():
    rooms = [
        Room(0, "start"),
        Room(1, "middle"),
        Room(2, "exit")
    ]
    dungeon = Dungeon(rooms)

    moved = dungeon.move_forward()

    assert moved is True
    assert dungeon.position == 1
    assert dungeon.current_room() is rooms[1]


@pytest.mark.dungeon
def test_move_forward_in_last_room_is_impossible():
    rooms = [
        Room(0, "last")
    ]
    dungeon = Dungeon(rooms)

    dungeon.position = 0
    moved = dungeon.move_forward()

    assert moved is False
    assert dungeon.position == 0


@pytest.mark.dungeon
def test_move_back_success():
    rooms = [
        Room(0, "start"),
        Room(1, "last")
    ]
    dungeon = Dungeon(rooms)

    dungeon.position = 1
    moved = dungeon.move_back()

    assert moved is True
    assert dungeon.position == 0
    assert dungeon.current_room() is rooms[0]


@pytest.mark.dungeon
def test_move_back_in_start_room_is_impossible():
    rooms = [
        Room(0, "start")
    ]
    dungeon = Dungeon(rooms)

    dungeon.position = 0
    moved = dungeon.move_back()

    assert moved is False
    assert dungeon.position == 0


@pytest.mark.dungeon
def test_is_finished_from_last_room_is_true():
    rooms = [
        Room(0, "exit", is_exit_room=True)
    ]
    dungeon = Dungeon(rooms)

    dungeon.position = 0
    assert dungeon.is_finished() is True


@pytest.mark.dungeon
def test_is_finished_from_first_room_is_false():
    rooms = [
        Room(0, "start"),
    ]
    dungeon = Dungeon(rooms)

    assert dungeon.is_finished() is False


@pytest.mark.dungeon
def test_is_finished_from_middle_room_is_false():
    rooms = [
        Room(0, "start"),
        Room(1, "middle"),
        Room(2, "exit", is_exit_room=True)
    ]
    dungeon = Dungeon(rooms)

    dungeon.position = 1
    assert dungeon.is_finished() is False


@pytest.mark.dungeon
def test_dungeon_to_dict():
    rooms = [
        Room(0, "start"),
        Room(1, "exit", is_exit_room=True)
    ]
    dungeon = Dungeon(rooms)

    dungeon.position = 1
    room_in_dungeon = dungeon.to_dict()

    assert room_in_dungeon["position"] == 1
    assert isinstance(room_in_dungeon["rooms"], list)
    assert room_in_dungeon["rooms"][0]["number"] == 0
    assert room_in_dungeon["rooms"][1]["is_exit_room"] is True


@pytest.mark.dungeon
def test_dungeon_repr_does_not_crash():
    rooms = [
        Room(0, "start"),
        Room(1, "exit", is_exit_room=True)
    ]
    dungeon = Dungeon(rooms)

    text = repr(dungeon)

    assert "Dungeon(" in text
    assert "position =" in text
    assert "rooms =" in text
