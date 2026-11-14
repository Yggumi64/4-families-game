class Player:
    def __init__(self, name, n, faction, unite, castle_pos, life = 0, damage = 0):
        self._name = name
        self._number = n
        self._faction = faction
        self._unite = unite
        self._castle_pos = castle_pos
        self._life = life + faction.base_life
        self._damage = damage + faction.base_damage
        self._abilities = []
        if faction.passive_ability:
            self._abilities.append(faction.passive_ability)
            faction.passive_ability.on_ability_granted(self)
        self._target = self

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number
    
    @property
    def faction(self):
        return self._faction

    @property
    def unite(self):
        return self._unite

    @property
    def castle_pos(self):
        return self._castle_pos

    @property
    def life(self):
        return self._life

    @property
    def damage(self):
        return self._damage

    @property
    def ability(self):
        return self._ability

    @property
    def target(self):
        return self._target

    def set_target(self, target : "Player"):
        self._target = target

    def alterLife(self, amount):
        self._life += amount
        self._life = max(self._life, 0)
        if amount > 0:
            print(f"{self.name} gain {amount} life")
        else:
            print(f"{self.name} lose {amount*(-1)} life")
        return self._life

    def alterDamage(self, amount):
        self._damage += amount
        self._damage = max(self._damage, 0)
        if amount > 0:
            print(f"{self.name} gain {amount} bonus damage")
        else:
            print(f"{self.name} lose {amount*(-1)} damage")
        return self._damage

    def take_damage(self, damage):
        for ability in self._abilities:
            ability.on_receive_damage(self, self._target)
        self.alterLife(-damage)
        return self._life

    def defend(self, targets):
        targeting_self = []
        for player in targets:
            if targets[player] == self and player != self:
                targeting_self.append(player)

        if len(targeting_self) != 0:
            for ability in self._abilities:
                ability.on_castle_defense(self, targeting_self)

        for ability in self._abilities:
            ability.on_defend(self, targets)

        # print(f"{self._name} choose defense.")
        return "defense"

    def encounter(self):
        # print(f"{self._name} have encountered {self._target.name}. They clash.")
        if self._target.target == self:
            for ability in self._abilities:
                ability.on_battle_clash(self, self._target)
            return "clash_on_battlefield"
        else:
            for ability in self._abilities:
                ability.on_castle_clash(self, self._target)
            return "clash_on_castle"

    def attack(self):
        for ability in self._abilities:
            ability.on_deal_damage(self, self._target)
        self._target.take_damage(self._damage)
        # print(f"{self._target.name} took {self._damage} damage. Remaining life: {self._target.life}.")
        return "attack"
        
    def mouvement(self, targets):
        if self._target.target is not None:
            # Se défend
            if self._target == self:
                self.defend(targets)

            # Attaque un joueur
            else:
                # print(f"{self._name} is moving towards {self._target.name}.")
                for ability in self._abilities:
                    ability.on_mouvement(self, targets)

                # clash
                if self._target.target == self._target or self._target.target == self:
                    self.encounter()

                # Parvient à attaquer un joueur
                else:
                    self.attack()
                    

    def get_bonuses(self, bonuses):
        for ability in bonuses:
            # print(f"{ability.name} granted to {self._name}")
            self._abilities.append(ability)
            ability.on_ability_granted(self)

    def start_turn(self):
        for ability in list(self._abilities):
            ability.on_turn_start(self)
            if not ability.lower_duration():
                self._abilities.remove(ability)
                self._abilities.on_removed_ability(self)
                print(f"{self._name}'s ability {ability.name} has expired.")


    def end_turn(self):
        for ability in self._abilities:
            ability.on_turn_end(self)

    def __str__(self):
        return f"Player: {self._name}, Faction: {self._faction.name}, Life: {self._life}, Damage: {self._damage}, Bonus: {[j.name for j in self._abilities]}"