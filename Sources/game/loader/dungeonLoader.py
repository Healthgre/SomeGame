import json
import random
from pathlib import Path

from game.dungeon.dungeon import Dungeon
from game.dungeon.room import Room
from game.loader.enemyLoader import load_enemy
from game.loader.playerLoader import load_player

path = Path(__file__).parent.parent / "json" / "data.json"


def load_dungeon(path: str):
    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        player = load_player(path)
        room_description = data["room_description"]
        enemies = [
            load_enemy(path),
            load_enemy(path),
            load_enemy(path)
        ]

        rooms = []
        total_rooms = 7

        for i in range(total_rooms):
            room = Room(
                number=i,
                description=random.choice(room_description),
                is_start_room=(i == 0),
                is_exit_room=(i == total_rooms - 1)

            )
            if i in {1, 3, 5}:
                room.spawn_enemy(enemies)

            rooms.append(room)

        dungeon = Dungeon(rooms)
        return dungeon


print(load_dungeon(path))
