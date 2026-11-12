import pygame

from game_factory import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("4 Mains - Choix simultanés")

player_choices = {
    "Player 1": None,
    "Player 2": None,
    "Player 3": None,
    "Player 4": None
}

p1 = Player("Player 1", pld)
p2 = Player("Player 2", vpr)
p3 = Player("Player 3", ext)
p4 = Player("Player 4", mag)

players = [p1, p2, p3, p4]

board = Board(players)
game = Game(players, board)

running = True
en_attente_des_choix = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and en_attente_des_choix:
            if event.key in KEY_MAPPING:
                player, choice = KEY_MAPPING[event.key]
                for p in players:
                    if choice == p.name:
                        player_choices[player] = p
                        print(f"{player} a choisi")
 
    if all(choice is not None for choice in player_choices.values()):
        en_attente_des_choix = False
        print("Tous les joueurs ont fait leur choix :")
        for player, target in player_choices.items():
            print(f"{player} a choisi {target.name}")
        game.play(player_choices)