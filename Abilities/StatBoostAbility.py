from typing import override

from Abilities.AbstractAbility import AbstractAbility


class StatBoostAbility(AbstractAbility):

    def __init__(self, name, description, life_boost, damage_boost, duration=None):
        super().__init__(name, description, duration, "StatBoostAbility")
        self._life_boost = life_boost
        self._damage_boost = damage_boost
        self._active = False

    @property
    def life_boost(self):
        return self._life_boost

    @property
    def damage_boost(self):
        return self._damage_boost

    @override
    def on_removed_ability(self, player):
        self._active = False
        player.alterLife(-self._life_boost)
        player.alterDamage(-self._damage_boost)

    @override
    def on_turn_start(self, player):
        if not self._active:
            self._active = True
            player.alterLife(self._life_boost)
            player.alterDamage(self._damage_boost)