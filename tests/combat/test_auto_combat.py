import pytest
from game.autoCombat.autoCombat import auto_combat
from game.player.player import Player
from game.player.playerWeapon import PlayerWeapon
from game.player.playerArmor import PlayerArmor
from game.enemy.enemy import Enemy
from game.enemy.enemyWeapon import EnemyWeapon
from game.enemy.enemyArmor import EnemyArmor


@pytest.mark.combat
def test_player_can_wins_in_auto_combat(capfd):
    player = Player(
        hp=10,
        description="test_hero_description",
        name="test_hero_name",
        weapon=PlayerWeapon("test_hero_weapon_name", "test_hero_description_weapon", damage=5, hit_chance=100),
        armor=PlayerArmor("test_hero_armor_name", "test_hero_description_armor", defense=0),
        death_description="test_hero_description_death",
    )
    enemy = Enemy(
        name="test_enemy_name",
        hp=5,
        description="test_enemy_description",
        death_description="test_hero_enemy_death",
        weapon=EnemyWeapon("test_enemy_weapon_namee", "test_enemy_description_weapon", damage=1, hit_chance=0),
        armor=EnemyArmor("test_enemy_armor_name", "test_enemy_description_armor", defense=0)
    )

    auto_combat(player, enemy)
    # Про это надо почитать, доразобраться,
    out, _ = capfd.readouterr()
    assert "Победитель: test_hero_name" in out


@pytest.mark.combat
def test_auto_combat_enemy_wins(capfd):
    player = Player(
        hp=10,
        description="test_hero_description",
        name="test_hero_name",
        weapon=PlayerWeapon("test_hero_weapon_name", "test_hero_description_weapon", damage=1, hit_chance=0),
        armor=PlayerArmor("test_hero_armor_name", "test_hero_description_armor", defense=0),
        death_description="test_hero_description_death",
    )
    enemy = Enemy(
        name="test_enemy_name",
        hp=5,
        description="test_enemy_description",
        death_description="test_hero_enemy_death",
        weapon=EnemyWeapon("test_enemy_weapon_namee", "test_enemy_description_weapon", damage=5, hit_chance=100),
        armor=EnemyArmor("test_enemy_armor_name", "test_enemy_description_armor", defense=0)
    )

    auto_combat(player, enemy)
    # Главное не сломать!
    out, _ = capfd.readouterr()
    assert "Победитель: test_enemy_name" in out

# Хорошо бы тест на ничью сделать, но у меня так прописано, что шанса на ничью НЕТ!
