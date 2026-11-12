from Abilities.StatBoostAbility import StatBoostAbility
from Board import Board
from Entities.Faction import Faction
from Entities.Player import Player
from Game import Game

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

print(p1)
print(p2)
print(p3)
print(p4)

players = [p1, p2, p3, p4]

board = Board(players)

game = Game(players, board)

game.play()