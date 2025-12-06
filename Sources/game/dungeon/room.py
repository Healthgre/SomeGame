import random

from game.enemy.enemy import Enemy


class Room:
    def __init__(self, number: int, description: str, enemy: Enemy = None, is_start_room: bool = False,
                 is_exit_room: bool = False):
        self.number = number
        self.description = description
        self.enemy = enemy
        self.is_start_room = is_start_room
        self.is_exit_room = is_exit_room

    def to_dict(self):
        return {
            "number": self.number,
            "description": self.description,
            "enemy": self.enemy.to_dict() if self.enemy else None,
            "is_start_room": self.is_start_room,
            "is_exit_room": self.is_exit_room
        }

    def __repr__(self):
        return (f"Room("
                f"\nnumber = {self.number},"
                f"\ndescription = '{self.description}',"
                f"\nenemy = {self.enemy},"
                f"\nis_start_room = {self.is_start_room},"
                f"\nis_exit_room = {self.is_exit_room})")

    def has_enemy(self):
        return bool(self.enemy and self.enemy.is_alive())

    def spawn_enemy(self, enemies):
        if not self.is_start_room and not self.is_exit_room:
            self.enemy = random.choice(enemies)
