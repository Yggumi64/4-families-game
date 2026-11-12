class AbstractAbility:
    def __init__(self, name, description, duration=None, type="AbstractAbility"):
        self._name = name
        self._description = description
        self._duration = duration
        self._type = type

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def duration(self):
        return self._duration

    @property
    def type(self):
        return self._type

    def lower_duration(self) -> bool:
        if self._duration is not None:
            self._duration -= 1
            return self._duration > 0
        return True

    def on_turn_start(self, player):
        pass

    def on_deal_damage(self, player, target):
        pass

    def on_mouvement(self, player, target):
        pass
    
    def on_receive_damage(self, player, source):
        pass

    def on_turn_end(self, player):
        pass

    def on_clash(self, player, target):
        pass

    def on_defend(self, player, target):
        pass

    def on_removed_ability(self, player):
        pass