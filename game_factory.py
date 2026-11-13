import pygame

from Abilities.StatBoostAbility import StatBoostAbility
from Entities.Faction import Faction
from Entities.Player import Player
from Entities.Unite import Unite

KEY_MAPPING = {
    # Joueur 1 (Zone AZQS)
    pygame.K_a: ("Player 1", "Player 1"),
    pygame.K_z: ("Player 1", "Player 2"),
    pygame.K_q: ("Player 1", "Player 3"),
    pygame.K_s: ("Player 1", "Player 4"),

    # Joueur 2 (Zone RTFG)
    pygame.K_r: ("Player 2", "Player 1"),
    pygame.K_t: ("Player 2", "Player 2"),
    pygame.K_f: ("Player 2", "Player 3"),
    pygame.K_g: ("Player 2", "Player 4"),

    # Joueur 3 (Zone YUHJ)
    pygame.K_y: ("Player 3", "Player 1"),
    pygame.K_u: ("Player 3", "Player 2"),
    pygame.K_h: ("Player 3", "Player 3"),
    pygame.K_j: ("Player 3", "Player 4"),

    # Joueur 4 (Zone OPLM)
    pygame.K_o: ("Player 4", "Player 1"),
    pygame.K_p: ("Player 4", "Player 2"),
    pygame.K_l: ("Player 4", "Player 3"),
    pygame.K_m: ("Player 4", "Player 4"),
}

SCREEN_SIZE = 800

life_boost_ability = StatBoostAbility("Life Boost", "Increases life by 3", 3, 0, None)
damage_boost_ability = StatBoostAbility("Damage Boost", "Increases damage by 1", 0, 1, None)

base_life = 12
base_damage = 3

pld = Faction("Paladin", "A holy warrior", "yellow", base_life, base_damage, life_boost_ability)
vpr = Faction("Vampire", "A bloodsucking creature of the night", "red", base_life, base_damage)
ext = Faction("Executioner", "A ruthless killer", "black", base_life, base_damage, damage_boost_ability)
mag = Faction("Mage", "A master of the arcane arts", "blue", base_life, base_damage)

u1 = Unite(100, 100)
u2 = Unite(SCREEN_SIZE-100, 100)
u3 = Unite(100, SCREEN_SIZE-100)
u4 = Unite(SCREEN_SIZE-100, SCREEN_SIZE-100)

p1 = Player("Player 1", pld, u1)
p2 = Player("Player 2", vpr, u2)
p3 = Player("Player 3", ext, u3)
p4 = Player("Player 4", mag, u4)

def export_players():
    return [p1, p2, p3, p4]