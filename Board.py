import random


class Board:
    def __init__(self, game_bonuses):
        self._board = self._create_board()
        self._game_bonuses = game_bonuses
        self._bonuses = {}
        self._players = []

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board

    @property
    def bonuses(self):
        return self._bonuses

    @players.setter
    def players(self, value):
        self._players = value

    def get_random_bonus(self):
        random.shuffle(self._game_bonuses)
        return self._game_bonuses[0]

    def _create_board(self):
        board = [['1', '?', 'X', '?', '2'],
                 ['?', '?', ' ', '?', '?'],
                 ['X', ' ', 'X', ' ', 'X'],
                 ['?', '?', ' ', '?', '?'],
                 ['3', '?', 'X', '?', '4']]
        return board

    def get_path_cells(self, start_pos, target_pos):
        x1, y1 = start_pos
        x2, y2 = target_pos
        
        path = []
        steps = max(abs(x2 - x1), abs(y2 - y1))
        if steps == 0:
            return [(x1, y1)]
            
        for i in range(steps + 1):
            curr_x = round(x1 + (x2 - x1) * (i / steps))
            curr_y = round(y1 + (y2 - y1) * (i / steps))
            path.append((curr_x, curr_y))
            
        return path

    def get_bonuses_in_path(self, start_grid_pos, target_grid_pos):
        path = self.get_path_cells(start_grid_pos, target_grid_pos)
        taken_bonuses = []
        print(f"bonus : {self._bonuses}, chemin : {path}")
        for pos in path:
            if pos in self._bonuses:
                taken_bonuses.append(self._bonuses[pos].ability)
                x, y = pos
                self._board[y][x] = '?' 
                del self._bonuses[pos]
        return taken_bonuses

    def spawn_random_bonus(self):
        empty_cells = []
        for y in range(len(self._board)):
            for x in range(len(self._board[y])):
                if self._board[y][x] == '?':
                    empty_cells.append((x, y))
                    
        if empty_cells:
            x, y = random.choice(empty_cells)
            self._board[y][x] = 'B'
            self._bonuses[(x, y)] = self.get_random_bonus()
            print(f"Un bonus est apparu en ({x}, {y}) !")

    def __str__(self):
        board_str = ""
        for row in self._board:
            board_str += " ".join(row) + "\n"
        return board_str