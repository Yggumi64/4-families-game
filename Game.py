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
            target = targets[player.name]
            player.set_target(target)
            player.unite.set_target_pos(target.unite.pos_x, target.unite.pos_y)

        for player in self._players:
            mvt = player.mouvement(targets)
            if mvt == "clash_on_battlefield":
                pos_x, pos_y = player.unite.get_midpoint(player._target.unite)
                player.unite.set_target_pos(pos_x, pos_y)
            bonuses = self._board.get_bonuses_in_path(player.castle_pos, target.castle_pos)
            print(player, bonuses)
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