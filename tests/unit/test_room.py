import pytest

from game.dungeon.room import Room
from game.enemy.enemy import Enemy


class FakeEnemy(Enemy):
    def __init__(self, alive=True):
        self._alive = alive

    def is_alive(self):
        return self._alive

    def to_dict(self):
        return {"alive": self._alive}

    def __repr__(self):
        return f"TestEnemy(alive={self._alive})"


@pytest.mark.room
def test_to_create_empty_room():
    room = Room(
        number=1,
        description="room_description",
        enemy=None,
        is_start_room=False,
        is_exit_room=False
    )

    assert room.number == 1
    assert room.description == "room_description"
    assert room.enemy is None
    assert room.is_start_room is False
    assert room.is_exit_room is False


@pytest.mark.room
def test_spawn_enemy_to_empty_room():
    room = Room(
        number=1,
        description="room_description",
        enemy=None,
        is_start_room=False,
        is_exit_room=False)

    enemy = FakeEnemy(alive=True)
    room.spawn_enemy(enemy)

    assert room.enemy is enemy
    assert isinstance(room.enemy, FakeEnemy)


@pytest.mark.room
def test_spawn_enemy_in_start_room_is_impossible():
    room = Room(0, "start_room", is_start_room=True)

    enemy = FakeEnemy()
    room.spawn_enemy(enemy)

    assert room.enemy is None


@pytest.mark.room
def test_spawn_enemy_in_exit_room_is_impossible():
    room = Room(6, "exit_room", is_exit_room=True)

    enemy = FakeEnemy()
    room.spawn_enemy(enemy)

    assert room.enemy is None


@pytest.mark.room
def test_room_has_alive_enemy():
    enemy = FakeEnemy(alive=True)
    room = Room(3, "test_room", enemy=enemy)

    assert room.has_enemy() is True


@pytest.mark.room
def test_room_has_dead_enemy():
    enemy = FakeEnemy(alive=False)
    room = Room(3, "test_room", enemy=enemy)

    assert room.has_enemy() is False


@pytest.mark.room
def test_room_to_dict():
    enemy = FakeEnemy(alive=True)
    room = Room(4, "test_room", enemy=enemy, is_start_room=False, is_exit_room=True)

    dungeon = room.to_dict()

    assert dungeon["number"] == 4
    assert dungeon["description"] == "test_room"
    assert dungeon["enemy"] == {"alive": True}
    assert dungeon["is_start_room"] is False
    assert dungeon["is_exit_room"] is True


@pytest.mark.room
def test_repr_does_not_crash():
    room = Room(1, "test_room", enemy=FakeEnemy())
    text = repr(room)

    assert "Room(" in text
    assert "number = 1" in text
    assert "test_room" in text
