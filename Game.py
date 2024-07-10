class Game:
    def guess(self, param: str):
        if param == None:
            raise ValueError("Arg must be List")
        if len(param) != 3:
            raise ValueError("Arg must be 3 digits")