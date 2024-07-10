from GameResult import GameResult


class Game:
    def __init__(self):
        self.question = "123"

    def set_question(self, question):
        self.question = question

    def get_length_of_question(self):
        return len(self.question)

    def is_correct(self, param):
        return self.question == param

    def is_strike(self, position, input_num):
        return position == self.question.find(input_num)

    def is_ball(self, input_num):
        if self.question.find(input_num) != -1:
            return True
        return False

    def guess(self, param: str):
        self.validation_of_arg(param)
        length = self.get_length_of_question()
        if self.is_correct(param):
            return GameResult(True, length, 0)

        strike = 0
        ball = 0
        length = self.get_length_of_question()
        for i in range(length):
            if self.is_strike(i, param[i]):
                strike += 1
            elif self.is_ball(param[i]):
                ball += 1

        return GameResult(False, strike, ball)

    def validation_of_arg(self, param):
        question_length = len(self.question)
        if param == None:
            raise ValueError("Arg must be List")
        if len(param) != question_length or not param.isdigit() or len(set(list(param))) != question_length:
            raise ValueError(f"Arg must be {question_length} different digits")
