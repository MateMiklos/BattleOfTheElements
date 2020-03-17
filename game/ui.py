def printGamingData(turn, player1, player2, playerOnTurn):
    print('*****************************************************************')
    print('=================================================================')
    print('It is turn ' + str(turn))
    print('It is ' + playerOnTurn.getName() + '\'s turn')
    print('=================================================================')
    print('Player1 LIFE: ' + str(player1.getLifeTotal()) + ' MANA: ' + str(player1.getManaTotal()))
    print('Player2 LIFE: ' + str(player2.getLifeTotal()) + ' MANA: ' + str(player2.getManaTotal()))
    print('=================================================================')
    print('*****************************************************************')


def printPlayerDeck(player):
    deck = player.getDeck()
    print('*****************************************************************')
    print('=================================================================')
    print(player.getName() + '\'s decklist:')
    for card in deck.cards:
        print(card)
    print('=================================================================')
    print(player.getName() + '\'s discardpile:')
    for card in deck.discardPile:
        print(card)
    print('=================================================================')
    print('*****************************************************************')
    