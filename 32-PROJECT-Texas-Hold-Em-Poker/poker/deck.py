from poker.card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def shuffle(self):
        """
        another way to do this would be by dependecy injection
        and passing the random.shuffle function as a parameter
        """
        random.shuffle(self.cards)

    def remove_cards(self, number):
        cards_to_remove = self.cards[:number]
        del self.cards[:number]
        return cards_to_remove
