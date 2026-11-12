import pygame

import Board
import Game
from Abilities.StatBoostAbility import StatBoostAbility
from Entities.Faction import Faction
from Entities.Player import Player

# Dictionnaire global pour mapper chaque touche à un (joueur, action/cible)
KEY_MAPPING = {
    # Joueur 1 (Zone AZQS)
    pygame.K_a: ("J1", "Cible_1"),
    pygame.K_z: ("J1", "Cible_2"),
    pygame.K_q: ("J1", "Cible_3"),
    pygame.K_s: ("J1", "Cible_4"),
    
    # Joueur 2 (Zone RTFG)
    pygame.K_r: ("J2", "Cible_1"),
    pygame.K_t: ("J2", "Cible_2"),
    pygame.K_f: ("J2", "Cible_3"),
    pygame.K_g: ("J2", "Cible_4"),
    
    # Joueur 3 (Zone YUHJ)
    pygame.K_y: ("J3", "Cible_1"),
    pygame.K_u: ("J3", "Cible_2"),
    pygame.K_h: ("J3", "Cible_3"),
    pygame.K_j: ("J3", "Cible_4"),
    
    # Joueur 4 (Zone OPLM)
    pygame.K_o: ("J4", "Cible_1"),
    pygame.K_p: ("J4", "Cible_2"),
    pygame.K_l: ("J4", "Cible_3"),
    pygame.K_m: ("J4", "Cible_4"),
}

life_boost_ability = StatBoostAbility("Life Boost", "Increases life by 3", 3, 0, None)
damage_boost_ability = StatBoostAbility("Damage Boost", "Increases damage by 1", 0, 1, None)

base_life = 12
base_damage = 3

pld = Faction("Paladin", "A holy warrior", base_life, base_damage, life_boost_ability)
vpr = Faction("Vampire", "A bloodsucking creature of the night", base_life, base_damage)
ext = Faction("Executioner", "A ruthless killer", base_life, base_damage, damage_boost_ability)
mag = Faction("Mage", "A master of the arcane arts", base_life, base_damage)

p1 = Player("Player 1", pld)
p2 = Player("Player 2", vpr)
p3 = Player("Player 3", ext)
p4 = Player("Player 4", mag)

players = [p1, p2, p3, p4]

def create_game():
    board = Board(players)
    game = Game(players, board)
    return game