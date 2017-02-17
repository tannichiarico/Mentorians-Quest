#!python
from classes import Healer, Warrior, Shaman


john = Warrior('John', 10)
troy = Shaman('Troy', 15)
ari = Healer('Ari', 3)

john.attack(troy)
john.move(13)
john.attack(troy)
