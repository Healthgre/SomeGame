import json
import random

from game.player import Player

print("Игра запустилась.")

random_enemy = random.randint(1,3)



with open("json/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)

# a = EnemyWeapon()
# print(a)
