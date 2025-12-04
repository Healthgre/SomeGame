import json
import random


from game.dungeon import Dungeon
from game.enemyWeapon import EnemyWeapon
from game.player import Player

print("Игра запустилась.")

random_enemy = random.randint(1,3)



with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)

# a = EnemyWeapon()
# print(a)
