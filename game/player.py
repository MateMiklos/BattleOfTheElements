class Player:

    def __init__(self, name, deck):
        self.__deck = deck
        self.__name = name
        self.__lifeTotal = 30
        self.__manaTotal = 30

    def getDeck(self):
        return self.__deck

    def getName(self):
        return self.__name

    def getLifeTotal(self):
        return self.__lifeTotal
        
    def getManaTotal(self):
        return self.__manaTotal

    def setName(self, name):
        self.__name = name
        
    def setLifeTotal(self, lifeTotal):
        self.__lifeTotal = lifeTotal

    def setManaTotal(self, manaTotal):
        self.__manaTotal = manaTotal
