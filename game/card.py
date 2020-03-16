class Card:

    def __init__(self, name, manacost, elementType, spellType, abilityDescription):
        self.__name = name
        self.__manacost = manacost
        self.__elementType = elementType
        self.__spellType = spellType
        self.__abilityDescription = abilityDescription

    def getName(self):
        return self.__name

    def getManacost(self):
        return self.__manacost

    def getElementType(self):
        return self.__elementType

    def getSpellType(self):
        return self.__spellType

    def getAbilityDiscription(self):
        return self.__abilityDescription


card1 = Card('Fireball', 4, 'FIRE', 'INSTANT', 'Deals 6 damage')
card2 = Card('Spring', 4, 'WATER', 'INSTANT', 'Heals 6 damage')
card3 = Card('Sprint', 1, 'AIR', 'INSTANT', 'Gain 3 mana')
card4 = Card('Immobilize', 2, 'EARTH', 'INSTANT', 'Drain 3 mana')
card5 = Card('Fireball', 4, 'FIRE', 'INSTANT', 'Deals 6 damage')
card6 = Card('Spring', 4, 'WATER', 'INSTANT', 'Heals 6 damage')
card7 = Card('Sprint', 1, 'AIR', 'INSTANT', 'Gain 3 mana')
card8 = Card('Immobilize', 2, 'EARTH', 'INSTANT', 'Drain 3 mana')
card9 = Card('Fireball', 4, 'FIRE', 'INSTANT', 'Deals 6 damage')
card10 = Card('Spring', 4, 'WATER', 'INSTANT', 'Heals 6 damage')
card11 = Card('Sprint', 1, 'AIR', 'INSTANT', 'Gain 3 mana')
card12 = Card('Immobilize', 2, 'EARTH', 'INSTANT', 'Drain 3 mana')
