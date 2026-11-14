from typing import override

from Abilities.AbstractAbility import AbstractAbility


class ThornAbility(AbstractAbility):
    def __init__(self, name, description, value, duration=None):
        super().__init__(name, description, duration, "ThornAbility")
        self._value = value

    @property
    def value(self):
        return self._value

    @override
    def on_castle_defense(self, player, targets):
        for target in targets:
            self.thorn_log(player, target)
            target.alterLife(-self._value)

    def thorn_log(self, player, target):
        print(f"{player.name} spike {target.name} for {self._value} damage")