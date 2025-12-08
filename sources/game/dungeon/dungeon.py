from game.dungeon.room import Room


class Dungeon:
    def __init__(self, rooms: list[Room]):
        self.rooms = rooms
        self.position = 0

    def current_room(self):
        return self.rooms[self.position]

    def move_forward(self):
        if self.position < len(self.rooms) - 1:
            self.position += 1
            return True
        return False

    def move_back(self):
        if self.position > 0:
            self.position -= 1
            return True
        return False

    def is_finished(self):
        return self.current_room().is_exit_room

    def to_dict(self):
        return {
            "position": self.position,
            "rooms": [room.to_dict() for room in self.rooms]
        }

    def __repr__(self):
        return (
            "Dungeon("
            f"\nposition = {self.position},"
            f"\nrooms = {self.rooms}"
            "\n)"
        )
