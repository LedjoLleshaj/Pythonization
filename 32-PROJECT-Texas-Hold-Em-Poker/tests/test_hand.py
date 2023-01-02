import unittest
from poker.card import Card
from poker.hand import Hand
from poker.validators import PairValidator


class handTest(unittest.TestCase):
    def test_starts_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        ace_of_spades = Card(rank="Ace", suit="Spades")
        king_of_spades = Card(rank="King", suit="Spades")
        hand = Hand()
        hand.add_cards([ace_of_spades, king_of_spades])
        self.assertEqual(
            repr(hand),
            "King of Spades, Ace of Spades",
        )

    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank="Ace", suit="Spades")
        king_of_spades = Card(rank="King", suit="Spades")
        cards = [ace_of_spades, king_of_spades]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.cards, [king_of_spades, ace_of_spades])

    def test_interacts_with_validator_to_determine_winning_hand(self):
        class HandWithOneValidator(Hand):
            VALIDATORS = (PairValidator,)  # comma is important to create the tuple

        hand = HandWithOneValidator()
        hand.add_cards(
            [
                Card(rank="Ace", suit="Spades"),
                Card(rank="Ace", suit="Clubs"),
            ]
        )
        self.assertEqual(hand.best_rank(), "Pair")
