class Board:
    def __init__(self, players):
        self._players = players
        self._board = self._create_board()

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board

    def _create_board(self):
        board = [['1', '?', 'X', '?', '2'],
                 ['?', '?', ' ', '?', '?'],
                 ['X', ' ', 'X', ' ', 'X'],
                 ['?', '?', ' ', '?', '?'],
                 ['3', '?', 'X', '?', '4']]
        return board

    def __str__(self):
        board_str = ""
        for row in self._board:
            board_str += " ".join(row) + "\n"
        return board_str