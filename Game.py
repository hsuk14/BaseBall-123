from GameResult import GameResult


class Game:
    def __init__(self):
        self.question = None

    def set_question(self, question):
        self.question = question

    def guess(self, param: str):
        self.validation_of_arg(param)
        strike = 0
        ball = 0
        solved = False
        for i in range(3):
            for j in range(3):
                if self.question[i] == param[j]:
                    if i == j:
                        strike += 1
                    else:
                        ball += 1
        if strike == 3:
            solved = True
        return GameResult(solved, strike, ball)

    def validation_of_arg(self, param):
        if param == None:
            raise ValueError("Arg must be List")
        if len(param) != 3 or not param.isdigit() or len(set(list(param))) != 3:
            raise ValueError("Arg must be 3 different digits")
