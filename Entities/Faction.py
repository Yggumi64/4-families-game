class Faction:
    def __init__(self, name, description, color, life, damage, passive_ability=None):
        self._name = name
        self._description = description
        self._color = color
        self._base_life = life
        self._base_damage = damage
        self._passive_ability = passive_ability

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def base_life(self):
        return self._base_life

    @property
    def base_damage(self):
        return self._base_damage

    @property
    def passive_ability(self):
        return self._passive_ability

    @property
    def color(self):
        return self._color

    def __str__(self):
        return f"Faction: {self._name}, Description: {self._description}, Life: {self._base_life}, Damage: {self._base_damage}, Passive Ability: {self._passive_ability.name if self._passive_ability else 'None'}"