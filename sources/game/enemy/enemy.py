from game.enemy.enemyArmor import EnemyArmor
from game.enemy.enemyWeapon import EnemyWeapon


class Enemy:
    def __init__(self, name: str, hp: int, description: str, death_description: str, weapon: EnemyWeapon = None,
                 armor: EnemyArmor = None):
        self.name = name
        self.hp = hp
        self.description = description
        self.death_description = death_description
        self.weapon = weapon or EnemyWeapon("Без оружия", 0, "Нет описания", 0)
        self.armor = armor or EnemyArmor("Без брони", "Нет описания", 0)

    def __repr__(self):
        return (f"Enemy("
                f"\nname = {self.name},"
                f"\nhp = {self.hp},"
                f"\ndescription = {self.description},"
                f"\ndeath_description = {self.death_description},"
                f"\nweapon = {self.weapon},"
                f"\narmor = {self.armor})")

    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "description": self.description,
            "death_description": self.death_description,
            "weapon": self.weapon.to_dict(),
            "armor": self.armor.to_dict()
        }

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage: int):
        armor = self.armor.defense
        final_damage = max(0, damage - armor)
        self.hp = max(0, self.hp - final_damage)
        return final_damage
