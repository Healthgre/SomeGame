import random

from game.enemy.enemy import Enemy
from game.player.player import Player


def auto_combat(player: Player, enemy: Enemy):
    print(f"{'=' * 100} Автобой начался {'=' * 100}")

    attacker = player
    defender = enemy

    while player.is_alive() and enemy.is_alive():
        print(f"{attacker.name} атакует {defender.name}!")
        print("-" * 300)

        positive_chance = attacker.weapon.hit_chance
        negative_chance = 100 - positive_chance
        all_chances = ((["hit"] * positive_chance) + (["miss"] * negative_chance))

        if random.choice(all_chances) == "hit":
            damage = attacker.weapon.damage
            defender.take_damage(damage)
            print(f"Попадание! Урон: {damage}. HP {defender.name}: {defender.hp}")
        else:
            print(f"{attacker.name} промахнулся!")

        if defender.is_alive():
            attacker, defender = defender, attacker
        else:
            print(f"\n{defender.name} повержен!")
            break

    print(f"\n{'=' * 100} Автобой завершён {'=' * 100}")

    winner = player if player.is_alive() else enemy
    print(f"Победитель: {winner.name}")
