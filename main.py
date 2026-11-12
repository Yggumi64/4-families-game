import pygame

from Board import Board
from Game import Game
from game_factory import export_players, KEY_MAPPING, SCREEN_SIZE

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("4 Mains - Choix simultanés")

player_choices = {
    "Player 1": None,
    "Player 2": None,
    "Player 3": None,
    "Player 4": None
}

players = export_players()

board = Board(players)
game = Game(players, board)

running = True
en_attente_des_choix = True
clock = pygame.time.Clock()
SPEED_LINE = 150

while running:

    # Init screen
    dt = clock.tick(60) / 1000

    screen.fill("purple")

    for player in players:# Init screen
        pygame.draw.circle(screen, player.faction.color, player.unite.pos, 40)

    # Ask for target
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

    # Play a turn
    if all(choice is not None for choice in player_choices.values()):
        en_attente_des_choix = False
        #print("Tous les joueurs ont fait leur choix :")
        #for player, target in player_choices.items():
            #print(f"{player} a choisi {target.name}")
        game.play(player_choices)

        arrived = 0
        for player in players:
            if player.unite.move_to(dt, SPEED_LINE):
                arrived += 1

        if arrived == len(players):
            en_attente_des_choix = True
            for player in players:
                player.set_target(player)
            player_choices = {player.name: None for player in players}
        

    pygame.display.flip()