from game.player.playerArmor import PlayerArmor
from game.player.playerWeapon import PlayerWeapon


class Player:
    def __init__(self, hp: int, description: str, name: str, weapon: PlayerWeapon, armor: PlayerArmor,
                 death_description: str):
        self.hp = hp
        self.description = description
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.death_description = death_description

    def is_alive(self):
        return self.hp > 0

    def to_dict(self):
        return {
            "hp": self.hp,
            "description": self.description,
            "name": self.name,
            "weapon": self.weapon.to_dict(),
            "armor": self.armor.to_dict(),
            "death_description": self.death_description,
        }

    def __repr__(self):
        return (f"Player("
                f"\nhp = {self.hp},"
                f"\ndescription = {self.description},"
                f"\nname = {self.name},"
                f"\nweapon = {self.weapon},"
                f"\narmor = {self.armor},"
                f"\ndeath_description = {self.death_description})")
