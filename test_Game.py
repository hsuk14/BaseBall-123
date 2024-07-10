from unittest import TestCase

from Game import Game
from GameResult import GameResult


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.sut = Game()

    def assert_illegal_arg(self, input_word, expected_result):
        with self.assertRaises(ValueError) as ve:
            self.sut.guess(input_word)
        self.assertEqual(expected_result, str(ve.exception))

    def test_raise_exception_when_input_is_none(self):
        self.assert_illegal_arg(None, "Arg must be List")

    def test_raise_exception_when_input_length_is_not_proper(self):
        self.assert_illegal_arg("12", "Arg must be 3 different digits")
        self.assert_illegal_arg("abc", "Arg must be 3 different digits")
        self.assert_illegal_arg("121", "Arg must be 3 different digits")

    def test_return_solved_result_if_correct(self):
        self.sut.set_question("123")
        result: GameResult = self.sut.guess("123")

        self.assertIsNotNone(result)
        self.assertTrue(result.get_solved())
        self.assertEqual(3, result.get_strike())
        self.assertEqual(0, result.get_ball())

    def test_return_unsolved_result_if_all_incorrect(self):
        self.sut.set_question("123")
        result: GameResult = self.sut.guess("456")

        self.assertIsNotNone(result)
        self.assertFalse(result.get_solved())
        self.assertEqual(0, result.get_strike())
        self.assertEqual(0, result.get_ball())


    def test_return_proper_value_if_2_strike_0_ball(self):
        self.sut.set_question("123")
        result: GameResult = self.sut.guess("143")

        self.assertIsNotNone(result)
        self.assertFalse(result.get_solved())
        self.assertEqual(2, result.get_strike())
        self.assertEqual(0, result.get_ball())

    def test_return_proper_value_if_0_strike_2_ball(self):
        self.sut.set_question("123")
        result: GameResult = self.sut.guess("312")

        self.assertIsNotNone(result)
        self.assertFalse(result.get_solved())
        self.assertEqual(0, result.get_strike())
        self.assertEqual(3, result.get_ball())

    def test_return_proper_value_if_4_digit(self):
        self.sut.set_question("1234")
        result: GameResult = self.sut.guess("3124")

        self.assertIsNotNone(result)
        self.assertFalse(result.get_solved())
        self.assertEqual(1, result.get_strike())
        self.assertEqual(3, result.get_ball())
