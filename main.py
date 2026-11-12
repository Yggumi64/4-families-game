import pygame

from game_factory import create_game

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("4 Mains - Choix simultanés")

player_choices = {
    "Player 1": None,
    "Player 2": None,
    "Player 3": None,
    "Player 4": None
}

running = True
en_attente_des_choix = True

create_game()  # Initialize the game and board