from exo_7.door import Door


class House(object):
    _surface: int = 0

    def __init__(self, surface: int, door_color: str):
        self._surface = surface
        self._door = Door(door_color)

    @property
    def surface(self) -> int:
        return self._surface

    @surface.setter
    def surface(self, value) -> None:
        self._surface = value

    def get_door(self) -> Door:
        return self._door

    def display(self):
        return f"Je suis une maison, ma surface est de {self.surface} m²"
