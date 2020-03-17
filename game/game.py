import player, deck, ability
import ui
from random import randint


# GLOBAL VARIABLES


player1 = player.Player("Player1", deck.deck1)
player2 = player.Player("Player2", deck.deck2)
deck1 = player1.getDeck()
deck2 = player2.getDeck()


# GAME MECHANICS


def dealBoard(deck):
    for i in range(deck.boardSize):
        randIndex = randint(0, len(deck.cards) - 1)
        deck.board.append(deck.cards[randIndex])
        deck.cards.remove(deck.cards[randIndex])


def selectCard(board, player, playerInput):
    if canBeSelected(board[playerInput], player):
        selectedCard = board[playerInput]
        return selectedCard
    selectCard(board, player, playerInput)


def canBeSelected(card, player):
    if card.getManacost() <= player.getManaTotal():
        return True
    return False


def castSelectedCard(card, playerOnTurn, playerOnOpposite):
    abilityToCast = getattr(ability, card.getName().lower())
    abilityToCast(playerOnTurn, playerOnOpposite)


def distributeCards(deck, selectedCard):
    deck.board.remove(selectedCard)
    for card in deck.board:
        deck.discardPile.append(card)
    deck.board = []


def getPlayerOnTurn():
    if turn % 2 == 0:
        return player2
    return player1


def getPlayerOnOpposite(playerOnTurn):
    if playerOnTurn == player1:
        return player2
    return player1


def getPlayerInput():
    playerInput = input('Select card!')
    return int(playerInput)


def printBoard(board):
    for card in board:
        print(card.getName())


def listAbilities():
    print(dir(ability))


# THE GAME


def game():
    turn = 0
    while player1.getLifeTotal() > 0 or player2.getLifeTotal() > 0:
        turn += 1
        if turn % 2 == 0:
            playerOnTurn = player2
            playerOnOpposite = player1
        else:
            playerOnTurn = player1
            playerOnOpposite = player2
        deck = playerOnTurn.getDeck()

        ui.printGamingData(turn, player1, player2, playerOnTurn)

        dealBoard(deck)
        printBoard(deck.board)
        playerInput = getPlayerInput()
        selectedCard = selectCard(deck.board, playerOnTurn, playerInput)
        castSelectedCard(selectedCard, playerOnTurn, playerOnOpposite)
        distributeCards(deck, selectedCard)

        ui.printPlayerDeck(playerOnTurn)
        ui.printPlayerDeck(playerOnOpposite)

    print('GAME OVER')


game()
