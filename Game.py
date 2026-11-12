class Game:
    def __init__(self, players, board):
        self._players = players
        self._board = board

    def play(self):
        targets = {player.name: player for player in self._players}
        for player in self._players:
            player.start_turn()
            target = input(f"{player.name}, press a player number you want to target: ")
            target_player = self._players[int(target) - 1]
            player.set_target(target_player)
            targets[player.name] = target_player

        for player in self._players:
            player.mouvement(targets)
            
        for player in self._players:
            player.end_turn()
        
        self.game_status()

    def game_status(self):
        for player in self._players:
            print(f"{player.name} - Remaining Life: {player.life}, Current Damage: {player.damage}")
        print(f"Board Status: \n{self._board}")

    def game_loop(self):
        while True:
            self.play()

    def __str__(self):
        return f"Game with players: {[player.name for player in self._players]} and board:\n{self._board}"