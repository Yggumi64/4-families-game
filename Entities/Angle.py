class Angle:
    def __init__(self):
        self._up_left = (0, 0)
        self._up_right = (1, 0)
        self._down_left = (0, 1)
        self._down_right = (1, 1)

    @property
    def up_right(self):
        return self._up_right

    @property
    def up_left(self):
        return self._up_left

    @property
    def down_right(self):
        return self._down_right

    @property
    def down_left(self):
        return self._down_left