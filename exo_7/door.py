class Door(object):
    _color: str = ""

    def __init__(self, color):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):
        self._color = value

    def display(self) -> str:
        return f"Je suis une porte, ma couleur est {self.color}"
