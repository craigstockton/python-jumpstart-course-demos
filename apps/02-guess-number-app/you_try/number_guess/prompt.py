class Prompt:
    def __init__(self):
        self.message = "Guess a number between 0 and 100: "

    def input(self):
        return int(input(self.message))
