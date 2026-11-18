class Game:
    def __init__(self, players, board):
        self._players = players
        self._player_choices = {player: None for player in players}
        self._player_by_name = {player.name: player for player in players}
        self._board = board
        self.CHOIX, self.ALLER, self.RETOUR = "choix", "aller", "retour"
        self.SPEED_LINE = 200
        self._state = self.CHOIX
        self._running = True
        
    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board

    @property
    def state(self):
        return self._state

    @property
    def player_choices(self):
        return self._player_choices

    @property
    def player_by_name(self):
        return self._player_by_name

    @property
    def running(self):
        return self._running

    def get_waiting_players(self):
        waiting_players = [j for j, choice in self._player_choices.items() if choice is None]
        return [j for j in self._players if j in waiting_players]

    def stop_game(self):
        self._running = False

    def set_targets(self, player, target):
        for p in self._players:
            if p.name == target and player in self._player_by_name:
                self._player_choices[self._player_by_name[player]] = p
                print(f"{player} a choisi sa cible.")

    def play(self):

        for player in self._players:
            player.start_turn()
            target = self._player_choices[player]
            player.set_target(target)
            player.unite.set_target_pos(target.unite.pos_x, target.unite.pos_y)

        for player in self._players:
            mvt = player.mouvement(self._player_choices)
            
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

    def check_dead_players(self):
        remaining_players = []
        for player in self._players:
            if player.life > 0:
                remaining_players.append(player)
        self._players = remaining_players
        return self._players

    def game_status(self):
        for player in self._players:
            print(f"{player.name} - Remaining Life: {player.life}, Current Damage: {player.damage}")
        print(f"Board Status: \n{self._board}")

    def four_player_logic(self, dt):
        if self._state == self.CHOIX:
            if all(choice is not None for choice in self._player_choices.values()):
                self.play()
                self._state = self.ALLER
    
        elif self._state == self.ALLER:
            arrives = [p.unite.move_to(p.unite.target_pos, dt, self.SPEED_LINE) for p in self._players]
            if all(arrives):
                self._state = self.RETOUR
    
        elif self._state == self.RETOUR:
            arrives = [p.unite.move_to(p.unite.home_pos, dt, self.SPEED_LINE) for p in self._players]
            if all(arrives):
                self.check_dead_players()
                for p in self._players:
                    p.set_target(p)
                self._player_choices = {p: None for p in self._players}
                self._player_by_name = {p.name:p for p in self._players}
                self._state = self.CHOIX
        
    def __str__(self):
        return f"Game with players: {[player.name for player in self._players]} and board:\n{self._board}"