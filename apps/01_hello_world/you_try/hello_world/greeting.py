class Greeting(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Nice to meet you {}".format(self.name)
