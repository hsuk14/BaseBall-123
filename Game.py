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

    def guess(self, param: str):
        self.validation_of_arg(param)
        if self.is_correct(param):
            return GameResult(True, 3, 0)

        strike = 0
        ball = 0
        for i in range(len(self.question)):
            for j in range(len(self.question)):
                if self.question[i] == param[j]:
                    if i == j:
                        strike += 1
                    else:
                        ball += 1

        return GameResult(False, strike, ball)

    def validation_of_arg(self, param):
        question_length = len(self.question)
        if param == None:
            raise ValueError("Arg must be List")
        if len(param) != question_length or not param.isdigit() or len(set(list(param))) != question_length:
            raise ValueError(f"Arg must be {question_length} different digits")
