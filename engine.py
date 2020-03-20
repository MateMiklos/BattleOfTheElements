from random import randint


# ===== CARD CLASS ===== #


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

    def getAbilityDescription(self):
        return self.__abilityDescription


# ===== DECK CLASS ===== #


class Deck:

    def __init__(self):
        self.cards = []
        self.board = []
        self.boardSize = 4
        self.ongoings = []
        self.ongoingsSize = 4
        self.discardPile = []


# ===== PLAYER CLASS ===== #


class Player:

    def __init__(self, name, deck):
        self.__name = name
        self.__deck = deck
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


# ===== PLAYER CLASS ===== #


class Game:

    def __init__(self, players):
        self.turn = 0
        self.player1 = players[0]
        self.player2 = players[1]


# ===== BUILD INSTANCES ===== #


def buildDecks():
    decks = []
    deck1 = Deck()
    deck2 = Deck()
    for i in range(10):
        deck1.cards.append(Card('Fireball', 4, 'FIRE', 'INSTANT', 'Deals 6 damage'))
        deck1.cards.append(Card('Spring', 4, 'WATER', 'INSTANT', 'Heals 6 damage'))
        deck1.cards.append(Card('Sprint', 1, 'AIR', 'INSTANT', 'Gain 3 mana'))
        deck1.cards.append(Card('Immobilize', 2, 'EARTH', 'INSTANT', 'Drain 3 mana'))
        deck2.cards.append(Card('Fireball', 4, 'FIRE', 'INSTANT', 'Deals 6 damage'))
        deck2.cards.append(Card('Spring', 4, 'WATER', 'INSTANT', 'Heals 6 damage'))
        deck2.cards.append(Card('Sprint', 1, 'AIR', 'INSTANT', 'Gain 3 mana'))
        deck2.cards.append(Card('Immobilize', 2, 'EARTH', 'INSTANT', 'Drain 3 mana'))
    decks.append(deck1)
    decks.append(deck2)
    return decks


def buildPlayers(decks):
    players = []
    player1 = Player('Player1', decks[0])
    player2 = Player('Player2', decks[1])
    players.append(player1)
    players.append(player2)
    return players


def buildGame(players):
    game = Game(players)
    return game


# ===== GAME MECHANICS ===== #


def dealBoard(deck):
    for i in range(deck.boardSize):
        try:
            randIndex = randint(0, len(deck.cards) - 1)
            deck.board.append(deck.cards[randIndex])
            deck.cards.remove(deck.cards[randIndex])
        except ValueError:
            for card in deck.cards:
                deck.board.append(card)
                deck.cards.remove(card)
