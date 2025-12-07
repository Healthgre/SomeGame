class EnemyWeapon:
    def __init__(self, name: str, description: str, damage: int, hit_chance: int):
        self.name = name
        self.damage = damage
        self.description = description
        self.hit_chance = hit_chance

    def to_dict(self):
        return {
            "name": self.name,
            "damage": self.damage,
            "description": self.description,
            "hit_chance": self.hit_chance,
        }

    def __repr__(self):
        return (f"EnemyWeapon("
                f"\n\tname = {self.name},"
                f"\n\tdamage = {self.damage},"
                f"\n\tdescription = {self.description},"
                f"\n\thit_chance = {self.hit_chance})")
