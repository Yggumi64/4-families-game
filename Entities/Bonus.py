class Bonus:
    def __init__(self, color, name, ability):
        self._color = color
        self._name = name
        self._ability = ability

    @property
    def color(self):
        return self._color
    
    @property
    def name(self):
        return self._name
    
    @property
    def ability(self):
        return self._ability

