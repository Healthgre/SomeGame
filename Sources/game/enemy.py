from game.enemyArmor import EnemyArmor
from game.enemyWeapon import EnemyWeapon


class Enemy:
    def __init__(self, name: str, hp: int, description: str, death_description: str, weapon: EnemyWeapon = "без оружия",
                 armor: EnemyArmor = "без брони"):
        self.name = name
        self.hp = hp
        self.description = description
        self.death_description = death_description
        self.weapon = weapon or EnemyWeapon()
        self.armor = armor or EnemyArmor()
