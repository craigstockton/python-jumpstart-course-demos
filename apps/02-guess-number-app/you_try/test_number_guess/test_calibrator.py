from number_guess.calibrator import Calibrator


def test_reconcile_equal():
    the_number = 71
    expected = {'is_equal': True, 'message': "Yes! You've got it. The number was 71"}
    actual = Calibrator(the_number).calibrate(the_number)
    assert expected == actual


def test_reconcile_high():
    the_number = 71
    guess = 72
    expected = {'is_equal': False, 'message': "Sorry but {} is HIGHER than the number".format(guess)}
    actual = Calibrator(the_number).calibrate(guess)
    assert expected == actual


def test_reconcile_low():
    guess = 70
    the_number = 71
    expected = {'is_equal': False, 'message': "Sorry but {} is LOWER than the number".format(guess)}
    actual = Calibrator(the_number).calibrate(guess)
    assert expected == actual
