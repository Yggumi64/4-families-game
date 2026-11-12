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

CHOIX, ALLER, RETOUR = "choix", "aller", "retour"
etat = CHOIX
SPEED_LINE = 150
clock = pygame.time.Clock()

while running:
    dt = clock.tick(60) / 1000

    # --- Événements ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and etat == CHOIX and event.key in KEY_MAPPING:
            joueur, cible = KEY_MAPPING[event.key]
            for p in players:
                if p.name == cible:
                    player_choices[joueur] = p
                    print(f"{joueur} a choisi {cible}")

    # --- Logique ---
    if etat == CHOIX:
        if all(c is not None for c in player_choices.values()):
            game.play(player_choices)
            etat = ALLER

    elif etat == ALLER:
        arrives = [p.unite.move_to(p.unite.target_pos, dt, SPEED_LINE) for p in players]
        if all(arrives):
            etat = RETOUR

    elif etat == RETOUR:
        arrives = [p.unite.move_to(p.unite.home_pos, dt, SPEED_LINE) for p in players]
        if all(arrives):
            game.play(player_choices)
            for p in players:
                p.set_target(p)
            player_choices = {p.name: None for p in players}
            etat = CHOIX

    # --- Dessin ---
    screen.fill("purple")
    for p in players:
        pygame.draw.circle(screen, p.faction.color, p.unite.pos, 40)
    pygame.display.flip()

pygame.quit()