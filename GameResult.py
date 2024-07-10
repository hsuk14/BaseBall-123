
class GameResult:
    def __init__(self, solved, strike, ball):
        self.solved = solved
        self.strike = strike
        self.ball = ball

    def set_strike(self, strike: int):
        self.strike = strike

    def set_ball(self, ball: int):
        self.ball = ball

    def set_solved(self, solved: bool):
        self.solved = solved

    def get_strike(self):
        return self.strike

    def get_ball(self):
        return self.ball

    def get_solved(self):
        return self.solved
