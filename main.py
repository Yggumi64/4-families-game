import pygame

from Game import Game
from game_factory import KEY_MAPPING, SCREEN_SIZE, export_game
from ScreenStorer import ScreenStorer

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Game Jam")
screen_storer = ScreenStorer()
screen_storer.screen = screen

player_choices = {
    "Player 1": None,
    "Player 2": None,
    "Player 3": None,
    "Player 4": None
}

players, board = export_game()
game = Game(players, board)
game.game_status()

running = True

CHOIX, ALLER, RETOUR = "choix", "aller", "retour"
etat = CHOIX
SPEED_LINE = 200
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
                    print(f"{joueur} a choisi sa cible.")

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
            for p in players:
                p.set_target(p)
            player_choices = {p.name: None for p in players}
            etat = CHOIX

    # --- Dessin ---
    screen.fill("gray")
    screen_storer.castle_value(players)
    screen_storer.draw_bonus(game.board)
    for p in players:
        p.unite.draw(screen, p)
    
    if etat == CHOIX:
        joueurs_en_attente = [j for j, c in player_choices.items() if c is None]
        joueurs_en_attente = [j for j in players if j.name in joueurs_en_attente]
        screen_storer.waiting_for_player(joueurs_en_attente)

    pygame.display.flip()

pygame.quit()