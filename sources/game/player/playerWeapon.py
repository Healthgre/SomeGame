class PlayerWeapon:
    def __init__(self, name: str, description: str, damage: int, hit_chance: int):
        self.name = name
        self.description = description
        self.damage = damage
        self.hit_chance = hit_chance

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "damage": self.damage,
            "hit_chance": self.hit_chance,
        }

    def __repr__(self):
        return (f"Player("
                f"\n\tname = {self.name},"
                f"\n\tdescription = {self.description},"
                f"\n\tdamage = {self.damage},"
                f"\n\thit_chance = {self.hit_chance})")
