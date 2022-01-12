from exo_7.apartment import Apartment
from exo_7.door import Door
from exo_7.house import House
from exo_7.person import Person

logement = House(150, "bleue")
appartement = Apartment("rouge")
thomas = Person("thomas", appartement)
jean = Person("jean", logement)

thomas.display()
print()
jean.display()


