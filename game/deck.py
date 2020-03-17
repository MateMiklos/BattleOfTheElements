import card


class Deck:

    maxDeckSize = 40

    def __init__(self):
        self.cards = []
        self.board = []
        self.boardSize = 4
        self.onGoings = []
        self.onGoingsSize = 4
        self.discardPile = []


# DECK BUILDING

deck1 = Deck()
deck2 = Deck()

for i in range(10):
    deck1.cards.append(card.Card('Fireball', 4, 'FIRE', 'INSTANT', 'Deals 6 damage'))
    deck1.cards.append(card.Card('Spring', 4, 'WATER', 'INSTANT', 'Heals 6 damage'))
    deck1.cards.append(card.Card('Sprint', 1, 'AIR', 'INSTANT', 'Gain 3 mana'))
    deck1.cards.append(card.Card('Immobilize', 2, 'EARTH', 'INSTANT', 'Drain 3 mana'))
    deck2.cards.append(card.Card('Fireball', 4, 'FIRE', 'INSTANT', 'Deals 6 damage'))
    deck2.cards.append(card.Card('Spring', 4, 'WATER', 'INSTANT', 'Heals 6 damage'))
    deck2.cards.append(card.Card('Sprint', 1, 'AIR', 'INSTANT', 'Gain 3 mana'))
    deck2.cards.append(card.Card('Immobilize', 2, 'EARTH', 'INSTANT', 'Drain 3 mana'))
