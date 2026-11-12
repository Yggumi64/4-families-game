class Player:
    def __init__(self, name, faction, unite, life = 0, damage = 0):
        self._name = name
        self._faction = faction
        self._unite = unite
        self._life = life + faction.base_life
        self._damage = damage + faction.base_damage
        self.abilities = []
        if faction.passive_ability:
            self.abilities.append(faction.passive_ability)
        self._target = self

    @property
    def name(self):
        return self._name

    @property
    def faction(self):
        return self._faction

    @property
    def unite(self):
        return self._unite

    @property
    def life(self):
        return self._life

    @property
    def damage(self):
        return self._damage

    @property
    def target(self):
        return self._target

    def set_target(self, target : "Player"):
        self._target = target

    def alterLife(self, amount):
        self._life += amount
        self._life = max(self._life, 0)
        return self._life

    def alterDamage(self, amount):
        self._damage += amount
        self._damage = max(self._damage, 0)
        return self._damage

    def take_damage(self, damage):
        for ability in self.abilities:
            ability.on_receive_damage(self, self._target)
        self.alterLife(-damage)
        return self._life
    
    def mouvement(self, targets):
        if self._target.target is not None:
            # Se défend
            if self._target == self:
                for ability in self.abilities:
                    ability.on_defend(self, targets)
                print(f"{self._name} choose defense.")

            # Attaque un joueur qui se défend
            else:
                for ability in self.abilities:
                    ability.on_mouvement(self, targets)

                # Rencontre un joueur lors de l'attaque
                target_action = self._target.target
                if target_action == self._target or target_action == self:
                    for ability in self.abilities:
                        ability.on_clash(self, targets)
                    print(f"{self._name} have encountered {self._target.name}. They clash.")

                # Parvient à attaquer un joueur
                else:
                    for ability in self.abilities:
                        ability.on_deal_damage(self, targets)
                    self._target.take_damage(self._damage)
                    print(f"{self._name} is moving towards {self._target.name}.")
                    print(f"{self._target.name} took {self._damage} damage. Remaining life: {self._target.life}.")


    def start_turn(self):
        self._life = self._faction.base_life
        self._damage = self._faction.base_damage
        for ability in list(self.abilities):
            ability.on_turn_start(self)
            if not ability.lower_duration():
                self.abilities.remove(ability)
                print(f"{self._name}'s ability {ability.name} has expired.")


    def end_turn(self):
        for ability in self.abilities:
            ability.on_turn_end(self)

    def __str__(self):
        return f"Player: {self._name}, Faction: {self._faction.name}, Life: {self._life}, Damage: {self._damage}"