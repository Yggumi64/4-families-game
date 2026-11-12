import pygame
from Entities.Player import Player


class Unite:
    def __init__(self, pos_x, pos_y):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._pos = pygame.Vector2(self._pos_x, self._pos_y)
        self._target_pos = pygame.Vector2(self._pos_x, self._pos_y)

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def pos(self):
        return self._pos

    @property
    def target_pos(self):
        return self._target_pos

    def set_target_pos(self, target_x, target_y):
        self._target_pos.update(target_x, target_y)

    def update_pos(self, x, y):
        self._pos_x += x
        self._pos_y += y
        self._pos.update(self._pos_x, self._pos_y)

    def is_diagonal(self):
        dx = self._target_pos.x - self._pos.x
        dy = self._target_pos.y - self._pos.y
        return dx != 0 and dy != 0

    def move_to(self, dt, speed):
        if self.is_diagonal():
            speed = ((speed**2)*2)**0.5
        direction = self._target_pos - self._pos
        distance = direction.length()
        step = speed * dt
        if distance <= step:
            self._pos.update(self._target_pos)
            return True
        self._pos += direction / distance * step
        return False