class Game:
    def guess(self, param: str):
        self.validation_of_arg(param)

    def validation_of_arg(self, param):
        if param == None:
            raise ValueError("Arg must be List")
        if len(param) != 3 or not param.isdigit() or len(set(list(param))) != 3:
            raise ValueError("Arg must be 3 different digits")

