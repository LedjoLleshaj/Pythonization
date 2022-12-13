import unittest
from unittest.mock import MagicMock


class Actor:
    def jump_out_of_helicopter(self):
        return "Hell naw!"

    def light_on_fire(self):
        return "Wtf"


class Movie:
    def __init__(self, actor):
        self.actor = actor

    def start_filming(self):
        self.actor.jump_out_of_helicopter()
        self.actor.light_on_fire()


class MovieTests(unittest.TestCase):
    def test_start_filming(self):
        actor = MagicMock()
        movie = Movie(actor)
        movie.start_filming()
        actor.jump_out_of_helicopter.assert_called_once()
        actor.light_on_fire.assert_called_once()


if __name__ == "__main__":
    unittest.main()
