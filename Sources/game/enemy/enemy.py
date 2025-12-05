from game.enemy.enemyArmor import EnemyArmor
from game.enemy.enemyWeapon import EnemyWeapon


class Enemy:
    def __init__(self, name: str, hp: int, description: str, death_description: str, weapon: EnemyWeapon = None,
                 armor: EnemyArmor = None):
        self.name = name
        self.hp = hp
        self.description = description
        self.death_description = death_description
        self.weapon = weapon or EnemyWeapon("Без оружия", "Нет описания", 0, 0)
        self.armor = armor or EnemyArmor("Без брони", "Нет описания", 0)

    def is_alive(self):
        return self.hp > 0

    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "description": self.description,
            "death_description": self.death_description,
            "weapon": self.weapon.to_dict(),
            "armor": self.armor.to_dict()
        }