from game.playerArmor import PlayerArmor
from game.playerWeapon import PlayerWeapon


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
