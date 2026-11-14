class Game:
    def __init__(self, players, board):
        self._players = players
        self._board = board

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board

    def play(self, targets):

        for player in self._players:
            player.start_turn()
            target = targets[player]
            player.set_target(target)
            player.unite.set_target_pos(target.unite.pos_x, target.unite.pos_y)

        for player in self._players:
            mvt = player.mouvement(targets)
            
            target_grid_pos = player.target.castle_pos
            if mvt == "clash_on_battlefield":
                pos_x, pos_y = player.unite.get_midpoint(player._target.unite)
                player.unite.set_target_pos(pos_x, pos_y)

                x1, y1 = player.castle_pos
                x2, y2 = target_grid_pos
                target_grid_pos = (round((x1 + x2) / 2), round((y1 + y2) / 2))

            bonuses = self._board.get_bonuses_in_path(player.castle_pos, target_grid_pos)
            player.get_bonuses(bonuses)

        for player in self._players:
            player.end_turn()
        
        self.game_status()

        self._board.spawn_random_bonus()

    def game_status(self):
        for player in self._players:
            print(f"{player.name} - Remaining Life: {player.life}, Current Damage: {player.damage}")
        print(f"Board Status: \n{self._board}")

    def __str__(self):
        return f"Game with players: {[player.name for player in self._players]} and board:\n{self._board}"