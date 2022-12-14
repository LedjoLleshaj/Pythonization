class Hand:
    def __init__(self, cards):
        self.cards = cards

    def best_rank(self):
        card_rank_counts = {}
        for card in self.cards:
            # Ace of Spades
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1

        for rank, count in card_rank_counts.items():
            if count == 2:
                return "Pair"
        return "High Card"
