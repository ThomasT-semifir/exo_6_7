from exo_7.house import House


class Apartment(House):

    def __init__(self, door_color: str):
        super().__init__(50, door_color)

    def display(self) -> str:
        return f"Je suis un appartement, ma surface est {self.surface}"

    def se_plaindre_du_bruit_des_voisins_du_dessus(self):
        print("ils sont sérieux eux?")