from pathlib import Path

from game.loader.playerLoader import load_player
from game.loader.dungeonLoader import load_dungeon
from game.controller.controller import game_loop

if __name__ == "__main__":
    path = Path(__file__).parent / "game" / "json" / "data.json"

    print("Ищу JSON по пути:", path)

    player = load_player(str(path))
    dungeon = load_dungeon(str(path))

    game_loop(player, dungeon)
