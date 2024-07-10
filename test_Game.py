from unittest import TestCase

from Game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.sut = Game()

    def test_raise_exception_when_input_is_none(self):
        self.assert_illegal_arg(None, "Arg must be List")

    def test_raise_exception_when_input_length_is_not_proper(self):
        self.assert_illegal_arg("12", "Arg must be 3 digits")

    def assert_illegal_arg(self, input_word, expected_result):
        with self.assertRaises(ValueError) as ve:
            self.sut.guess(input_word)
        self.assertEqual(expected_result, str(ve.exception))

