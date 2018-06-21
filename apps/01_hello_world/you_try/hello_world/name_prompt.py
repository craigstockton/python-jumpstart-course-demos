class NamePrompt:
    def __init__(self):
        self.prompt = "What is your name?"

    def input(self):
        return input("{} ".format(self.prompt))
