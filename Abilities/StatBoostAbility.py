from typing import override

from Abilities.AbstractAbility import AbstractAbility


class StatBoostAbility(AbstractAbility):

    def __init__(self, name, description, life_boost, damage_boost, duration=None):
        super().__init__(name, description, duration, "StatBoostAbility")
        self._life_boost = life_boost
        self._damage_boost = damage_boost

    @property
    def life_boost(self):
        return self._life_boost

    @property
    def damage_boost(self):
        return self._damage_boost

    @override
    def on_removed_ability(self, player):
        if self._life_boost != 0:
            player.alterLife(-self._life_boost)
        if self._damage_boost != 0:
            player.alterDamage(-self._damage_boost)

    @override
    def on_ability_granted(self, player):
        if self._life_boost != 0:
            player.alterLife(self._life_boost)
        if self._damage_boost != 0:
            player.alterDamage(self._damage_boost)