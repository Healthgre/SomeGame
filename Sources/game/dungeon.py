class Dungeon:
    def __init__(self, map):
        self.level = map

    map = []

    def generate_map(self,map, rooms_count):
        self.map = map
        self.rooms_count = rooms_count
