import pygame


class ScreenStorer:
    def __init__(self):
        self.screen = None

    def set_screen(self, screen):
        self.screen = screen

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value

    def waiting_for_player(self, player_name):
        if self._screen is None:
            return

        width = self._screen.get_width()
        height = self._screen.get_height()

        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self._screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 36)
        text_surf = font.render(f"En attente de {player_name}...", True, (255, 255, 255))
        
        text_rect = text_surf.get_rect(center=(width // 2, height // 2))
        self._screen.blit(text_surf, text_rect)