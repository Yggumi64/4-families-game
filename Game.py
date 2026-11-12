class Game:
    def __init__(self, players, board):
        self._players = players
        self._board = board

    def play(self, targets):
        for player in self._players:
            player.start_turn()
            target = targets[player.name]
            player.set_target(target)
            player.unite.set_target_pos(target.unite.pos_x, target.unite.pos_y)

        for player in self._players:
            player.mouvement(targets)
            
        for player in self._players:
            player.end_turn()
        
        self.game_status()

    def game_status(self):
        for player in self._players:
            print(f"{player.name} - Remaining Life: {player.life}, Current Damage: {player.damage}")
        print(f"Board Status: \n{self._board}")

    def __str__(self):
        return f"Game with players: {[player.name for player in self._players]} and board:\n{self._board}"