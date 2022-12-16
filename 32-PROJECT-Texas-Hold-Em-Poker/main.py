# main lunching point of our program
from poker.card import Card
from poker.deck import Deck
from poker.player import Player
from poker.hand import Hand
from poker.game_round import GameRound

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()
player1 = Player("Ledjo", hand1)
player2 = Player("Bobby", hand2)
players = [player1, player2]

game_round = GameRound(deck=deck, players=players)
game_round.play()

# from main import deck, cards, hand1, hand2, player1, player2, game_round
