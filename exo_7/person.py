from exo_7.apartment import Apartment
from exo_7.house import House


class Person(object):
    _nom: str = ""
    _logement: House = None

    def __init__(self, nom: str, logement: House):
        self._nom = nom
        self._logement = logement

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, value: str) -> None:
        self._nom = value

    @property
    def logement(self) -> House:
        return self._logement

    def display(self):
        print(f"Je m'appelle {self.nom},\nvoici la description de mon logement: {self.logement.display()}\nvoici sa porte:{self.logement.get_door().display()}")
        self.se_plaindre()

    def se_plaindre(self):
        if(type(self.logement) is Apartment):
            self.logement.se_plaindre_du_bruit_des_voisins_du_dessus()
        else:
            print("Moi je suis une maison je n'ai pas de quoi me plaindre y'a personne pour m'embeter")
