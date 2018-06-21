from calibration import Calibration


class Calibrator(object):
    def __init__(self, comparator):
        self.comparator = comparator
        higher = "HIGHER"
        lower = "LOWER"
        self.equal_message = "Yes! You've got it. The number was {}"
        self.unequal_message = "Sorry but {} is %s than the number"
        self.high_message = self.unequal_message % higher
        self.low_message = self.unequal_message % lower

    def calibrate(self, the_number):
        is_equal = the_number == self.comparator
        if is_equal:
            message = self.equal_message.format(the_number)
        elif the_number > self.comparator:
            message = self.high_message.format(the_number)
        else:
            message = self.low_message.format(the_number)
        return Calibration(is_equal, message)
