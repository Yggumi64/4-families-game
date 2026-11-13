import pygame


class ScreenStorer:
    def __init__(self):
        self.screen = None

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value

    def castle_value(self, players):
        for p in players:
            angle = p.unite.angle

            dir_x = (angle[0] * 2) - 1
            dir_y = (angle[1] * 2) - 1
            
            pos_x = angle[0] * self._screen.get_width() - 40*dir_x
            pos_y = angle[1] * self._screen.get_height() - 40*dir_y
            pygame.draw.circle(self._screen, p.faction.color, pygame.Vector2(pos_x, pos_y), 40)
            
            font = pygame.font.Font(None, 36)
            text_surf = font.render(str(p.life), True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=(pos_x, pos_y))
            self._screen.blit(text_surf, text_rect)

    def waiting_for_player(self, players):
        if self._screen is None:
            return

        width = self._screen.get_width()
        height = self._screen.get_height()

        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self._screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 36)

        radius = 40
        diameter = radius * 2
        gap = 10
        num_players = len(players)

        total_width = num_players * diameter + (num_players - 1) * gap
        start_x = (width - total_width) // 2

        for i, player in enumerate(players):
            center_x = start_x + i * (diameter + gap) + radius
            center_y = height // 2

            pygame.draw.circle(self._screen, player.faction.color, (center_x, center_y), radius)
            pygame.draw.circle(self._screen, (255, 255, 255), (center_x, center_y), radius, 2)

            text_surf = font.render(str(player.number), True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=(center_x, center_y))
            self._screen.blit(text_surf, text_rect)

        text_surf_global = font.render("En attente des choix...", True, (255, 255, 255))
        text_rect_global = text_surf_global.get_rect(center=(width // 2, (height // 2) - 80))
        self._screen.blit(text_surf_global, text_rect_global)

    def transpos_board_to_screen(self, pos, board):
        if self._screen is None:
            return (0, 0)

        board_x, board_y = pos
        board_size = len(board.board)

        margin = 100
        width = self._screen.get_width() - (2 * margin)
        height = self._screen.get_height() - (2 * margin)

        step_x = width / (board_size-1)
        step_y = height / (board_size-1)

        screen_x = margin + (board_x * step_x)
        screen_y = margin + (board_y * step_y)

        return int(screen_x), int(screen_y)


    def draw_bonus(self, board):
        bonuses = board.bonuses
        for pos in bonuses:
            transpo_pos = self.transpos_board_to_screen(pos, board)
            color = bonuses[pos].color
            pygame.draw.circle(self._screen, color, transpo_pos, 40)