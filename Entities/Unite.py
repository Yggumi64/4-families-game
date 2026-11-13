import pygame


class Unite:
    def __init__(self, pos_x, pos_y):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._home_pos = pygame.Vector2(self._pos_x, self._pos_y)
        self._pos = pygame.Vector2(self._pos_x, self._pos_y)
        self._target_pos = pygame.Vector2(self._pos_x, self._pos_y)

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def home_pos(self):
        return self._home_pos

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

    def is_diagonal(self, target):
        dx = target.x - self._pos.x
        dy = target.y - self._pos.y
        return dx != 0 and dy != 0

    def get_midpoint(self, other_unite):
        pos = self._pos.lerp(other_unite.pos, 0.5)
        return int(pos.x), int(pos.y)

    def move_to(self, target, dt, speed):
        if self.is_diagonal(target):
            speed = ((speed**2)*2)**0.5
        direction = target - self._pos
        distance = direction.length()
        step = speed * dt
        if distance <= step:
            self._pos.update(target)
            return True
        self._pos += direction / distance * step
        return False