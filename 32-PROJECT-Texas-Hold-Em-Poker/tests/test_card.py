import unittest
from poker.card import Card


class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank="Queen", suit="Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank="Ace", suit="Spades")
        self.assertEqual(card.suit, "Spades")

    def test_knows_its_rank_index(self):
        card = Card(rank="Jack", suit="Hearts")
        self.assertEqual(card.rank_index, 9)

    def test_has_string_representation(self):
        card = Card(rank="Ace", suit="Spades")
        self.assertEqual(str(card), "Ace of Spades")

    def tests_has_technical_representation(self):
        card = Card(rank="Ace", suit="Spades")
        self.assertEqual(repr(card), "Card('Ace', 'Spades')")

    def test_card_has_four_possible_suits(self):

        self.assertEqual(Card.SUITS, ["Hearts", "Clubs", "Spades", "Diamonds"])

    def test_card_has_13_possible_ranks(self):
        self.assertEqual(
            Card.RANKS,
            [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "Jack",
                "Queen",
                "King",
                "Ace",
            ],
        )

    def test_card_only_accepts_valid_ranks(self):
        with self.assertRaises(ValueError):
            Card(rank="Two", suit="Spades")

    def test_card_only_accepts_valid_suits(self):
        with self.assertRaises(ValueError):
            Card(rank="Ace", suit="yolo")

    def test_can_create_standard_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)
        self.assertEqual(
            cards[0], Card(rank="2", suit="Hearts")
        )  # first card in the deck
        self.assertEqual(
            cards[-1], Card(rank="Ace", suit="Diamonds")
        )  # last card in the deck

    def test_figures_out_if_two_cards_are_equal(self):
        card1 = Card(rank="Ace", suit="Spades")
        card2 = Card(rank="Ace", suit="Spades")
        self.assertEqual(card1, card2)

    def test_card_can_sort_itself_with_another_one(self):
        two_of_spades = Card(rank="2", suit="Spades")
        five_of_diamonds = Card(rank="5", suit="Diamonds")
        self.assertEqual(
            two_of_spades < five_of_diamonds,
            True,
            "THe sort algorithm is not working properly",
        )

    def test_sorts_cards(self):
        two_of_spades = Card(rank="2", suit="Spades")
        five_of_diamonds = Card(rank="5", suit="Diamonds")
        five_of_hearts = Card(rank="5", suit="Hearts")
        eight_of_hearts = Card(rank="8", suit="Hearts")
        ace_of_clubs = Card(rank="Ace", suit="Clubs")

        unsorted_cards = [
            five_of_diamonds,
            two_of_spades,
            ace_of_clubs,
            five_of_hearts,
            eight_of_hearts,
        ]
        unsorted_cards.sort()
        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_diamonds,
                five_of_hearts,
                eight_of_hearts,
                ace_of_clubs,
            ],
        )
