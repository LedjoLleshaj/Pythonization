# main lunching point of our program
from poker.card import Card
from poker.deck import Deck
from poker.player import Player
from poker.hand import Hand

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand(cards=[])
hand2 = Hand(cards=[])
player1 = Player("Ledjo", hand1)
player2 = Player("Bobby", hand2)

# from main import deck, cards, hand1, hand2, player1, player2
