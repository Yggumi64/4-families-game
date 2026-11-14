import pygame

from Abilities.LifeStealOnClashAbility import LifeStealOnClashAbility
from Abilities.ThornAbility import ThornAbility
from Abilities.StatBoostAbility import StatBoostAbility
from Board import Board
from Entities.Angle import Angle
from Entities.Bonus import Bonus
from Entities.Faction import Faction
from Entities.Player import Player
from Entities.Unite import Unite

# Settings
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

# Factions
base_life = 12
base_damage = 3

life_boost_ability = StatBoostAbility("Life Boost", "Increases life by 3", 3, 0, None)
damage_boost_ability = StatBoostAbility("Damage Boost", "Increases damage by 1", 0, 1, None)
life_steal_ability = LifeStealOnClashAbility("Life Steal", "Regain life on clash", 1, None)
thorn_ability = ThornAbility("Thorn", "Inflict damage if castle is attacked", 1, None)

pld = Faction("Paladin", "A holy warrior", "yellow", base_life, base_damage, life_boost_ability)
vpr = Faction("Vampire", "A bloodsucking creature of the night", "red", base_life, base_damage, life_steal_ability)
ext = Faction("Executioner", "A ruthless killer", "black", base_life, base_damage, damage_boost_ability)
mag = Faction("Mage", "A master of the arcane arts", "blue", base_life, base_damage, thorn_ability)

# Bonus
temp_life_boost_ability = StatBoostAbility("Temporary Life Boost", "Increases life by 3", 3, 0, 2)
temp_damage_boost_ability = StatBoostAbility("Temporary Damage Boost", "Increases damage by 1", 0, 1, 2)
temp_life_steal_ability = LifeStealOnClashAbility("Temporary Life Steal", "Regain life on clash", 1, 2)
temp_thorn_ability = ThornAbility("Temporary Thorn", "Inflict damage if castle is attacked", 1, 2)

life_boost_bonus = Bonus("green", temp_life_boost_ability.name, temp_life_boost_ability)
damage_boost_bonus = Bonus("red", temp_damage_boost_ability.name, temp_damage_boost_ability)
life_steal_bonus = Bonus("purple", temp_life_steal_ability.name, temp_life_steal_ability)
thorn_bonus = Bonus("blue", temp_thorn_ability.name, temp_thorn_ability)

ALL_BONUSES = [life_boost_bonus, life_boost_bonus, life_boost_bonus, 
               damage_boost_bonus, damage_boost_bonus, damage_boost_bonus,
               life_steal_bonus,
               thorn_bonus, thorn_bonus
               ]

# Board init
board = Board(ALL_BONUSES)
BOARD_SIZE = len(board.board)

board.spawn_random_bonus()
board.spawn_random_bonus()
board.spawn_random_bonus()

# Unite
angles = Angle()
GAP = 100

u1 = Unite(angles.up_left, GAP, SCREEN_SIZE)
u2 = Unite(angles.up_right, GAP, SCREEN_SIZE)
u3 = Unite(angles.down_left, GAP, SCREEN_SIZE)
u4 = Unite(angles.down_right, GAP, SCREEN_SIZE)

# Player
MAX_INDEX = BOARD_SIZE-1

p1 = Player("Player 1", 1, pld, u1, (u1.angle[0]*MAX_INDEX, u1.angle[1]*MAX_INDEX))
p2 = Player("Player 2", 2, vpr, u2, (u2.angle[0]*MAX_INDEX, u2.angle[1]*MAX_INDEX))
p3 = Player("Player 3", 3, ext, u3, (u3.angle[0]*MAX_INDEX, u3.angle[1]*MAX_INDEX))
p4 = Player("Player 4", 4, mag, u4, (u4.angle[0]*MAX_INDEX, u4.angle[1]*MAX_INDEX))

# Game
players =  [p1, p2, p3, p4]
board.players = players

def export_game():
    return players, board