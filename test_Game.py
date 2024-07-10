from unittest import TestCase

from Game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.sut = Game()
    def test_raise_exception_when_input_is_none(self):
        with self.assertRaises(ValueError) as ve:
            self.sut.guess(None)
        self.assertEqual("Arg must be List", str(ve.exception))
