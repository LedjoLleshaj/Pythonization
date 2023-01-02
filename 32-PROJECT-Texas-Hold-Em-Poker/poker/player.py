class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def best_hand(self):
        return self.hand.best_rank()

    def add_cards(self, cards):
        self.hand.add_cards(cards)

    def wants_to_fold(self):
        return False

    def __gt__(self, other):
        """index is closer to 0, the better the hand"""
        return self.best_hand() < other.best_hand()
