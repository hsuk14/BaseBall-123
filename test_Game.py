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

    def test_raise_exception_when_input_length_is_not_proper(self):
        with self.assertRaises(ValueError) as ve:
            self.sut.guess("12")
        self.assertEqual("Arg must be 3 digits", str(ve.exception))
