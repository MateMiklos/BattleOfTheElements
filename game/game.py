import player, deck


player1 = player.Player("Player1", deck.deck)
player2 = player.Player("Player2", deck.deck)



deck = player1.getDeck()

print(deck)
print(player1.getName())

for elem in deck.cards:
    print(elem.getName())
    print(elem.getManacost())
    print(elem.getElementType())
