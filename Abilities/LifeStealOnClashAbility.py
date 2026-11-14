from typing import override

from Abilities.AbstractAbility import AbstractAbility


class LifeStealOnClashAbility(AbstractAbility):

    def __init__(self, name, description, value, duration=None):
        super().__init__(name, description, duration, "LifeStealOnClashAbility")
        self._value = value

    @property
    def value(self):
        return self._value

    @override
    def on_battle_clash(self, player, target):
        self.steal_log(player, target)
        player.alterLife(self._value)

    @override
    def on_castle_clash(self, player, target):
        self.steal_log(player, target)
        player.alterLife(self._value)

    @override
    def on_castle_defense(self, player, targets):
        for target in targets:
            self.steal_log(player, target)
            player.alterLife(self._value)

    def steal_log(self, player, target):
        print(f"{player.name} steal {self._value} life of {target.name} unit")