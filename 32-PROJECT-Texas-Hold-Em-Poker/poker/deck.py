from poker.card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def create_cards(self):
        cards = Card.create_standard_52_cards()

        # for suit in Card.SUITS:
        #     for rank in Card.RANKS:
        #         cards.append(Card(rank, suit))
        # this way deck class knows too much about card class
        # we want to have as much indipedence as possible between classes
        self.add_cards(cards)
