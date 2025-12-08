class EnemyArmor:
    def __init__(self, name: str, description: str, defense: int):
        self.name = name
        self.description = description
        self.defense = defense

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "defense": self.defense}

    def __repr__(self):
        return (f"EnemyArmor"
                f"\n\tname = {self.name},"
                f"\n\tdescription = {self.description},"
                f"\n\tdefense = {self.defense})")
