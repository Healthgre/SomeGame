from pathlib import Path

from game.autoCombat.autoCombat import auto_combat
from game.dungeon.dungeon import Dungeon
from game.player.player import Player
from game.loader.playerLoader import load_player
from game.loader.enemyLoader import load_enemy
from game.loader.dungeonLoader import load_dungeon


def game_loop(player: Player, dungeon: Dungeon):
    print("Игра началась!")
    print("Вы входите в подземелье...\n")

    while True:
        room = dungeon.current_room()
        print(f"\n{'=' * 300}")
        print(f"Вы находитесь в комнате {room.number}: {room.description}")

        if not player.is_alive():
            print("\n" + player.death_description)
            print("Игра окончена.")
            return

        if room.enemy and room.enemy.is_alive():
            enemy = room.enemy

            print(f"\nПеред вами враг: {enemy.name}")
            print(enemy.description)
            print(f"HP врага: {enemy.hp}")

            print("\nВыберите действие:")
            print("1. Атаковать")
            print("2. Убежать вперёд")
            print("3. Убежать назад")

            choice = input("> ")

            if choice == "1":
                print("\nВы вступили в бой!")
                auto_combat(player, enemy)

                if not player.is_alive():
                    print("\n" + player.death_description)
                    print("Игра окончена.")
                    return

                if not enemy.is_alive():
                    print(enemy.death_description)
                    room.enemy = None
                continue

            elif choice == "2":
                if dungeon.move_forward():
                    print("Вы убежали вперёд!")
                else:
                    print("Дальше идти некуда.")
                continue

            elif choice == "3":
                if dungeon.move_back():
                    print("Вы убежали назад!")
                else:
                    print("Назад идти некуда.")
                continue

            else:
                print("Неверный ввод.")
                continue

        print("\nКомната пуста.")

        if dungeon.is_finished():
            print("\nВы нашли выход из подземелья!")
            print("Поздравляем, вы победили!")
            return

        print("\nВыберите действие:")
        print("1. Пойти дальше")
        print("2. Вернуться назад")
        print("3. Выйти из подземелья")

        choice = input("> ")

        if choice == "1":
            if not dungeon.move_forward():
                print("Дальше идти некуда.")
        elif choice == "2":
            if not dungeon.move_back():
                print("Назад идти некуда.")
        elif choice == "3":
            print("Вы покинули подземелье.")
            return
        else:
            print("Неверный ввод.")
