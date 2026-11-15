import pygame

from Game import Game
from game_factory import KEY_MAPPING, SCREEN_SIZE, export_game
from ScreenManager import ScreenManager

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Game Jam")

screen_manager = ScreenManager()
screen_manager.screen = screen

players, board = export_game()
game = Game(players, board)
game.game_status()

clock = pygame.time.Clock()

while game.running:
    dt = clock.tick(60) / 1000

    # --- Événements ---
    screen_manager.event_manager(game, KEY_MAPPING)

    # --- Logique ---
    game.four_player_logic(dt)

    # --- Dessin ---
    screen_manager.draw_screen(game)

pygame.quit()