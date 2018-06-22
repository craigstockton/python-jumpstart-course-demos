import datetime

from birthday_calc import BirthdayCalc


def test_message_one_day_until():
    number_of_days = 1
    one_day = datetime.timedelta(days=number_of_days)
    birth_date = datetime.date.today() + one_day
    expected = "Looks like your birthday is in {} day.\nHope you're looking forward to it!".format(number_of_days)
    actual = BirthdayCalc(birth_date).birthday_message
    assert expected == actual


def test_message_one_day_ago():
    number_of_days = 1
    one_day = datetime.timedelta(days=number_of_days)
    birth_date = datetime.date.today() - one_day
    expected = "Looks like your birthday was {} day ago.\nHope you enjoyed your birthday!".format(abs(number_of_days))
    actual = BirthdayCalc(birth_date).birthday_message
    assert expected == actual


def test_message_today():
    expected = "HAPPY BIRTHDAY!!"
    actual = BirthdayCalc(datetime.date.today()).birthday_message
    assert expected == actual


def test_message_days_until():
    number_of_days = 2
    two_days = datetime.timedelta(days=number_of_days)
    birth_date = datetime.date.today() + two_days
    expected = "Looks like your birthday is in {} days.\nHope you're looking forward to it!".format(number_of_days)
    actual = BirthdayCalc(birth_date).birthday_message
    assert expected == actual


def test_message_days_past():
    number_of_days = 2
    two_days = datetime.timedelta(days=number_of_days)
    birth_date = datetime.date.today() - two_days
    expected = "Looks like your birthday was {} days ago.\nHope you enjoyed your birthday!".format(abs(number_of_days))
    actual = BirthdayCalc(birth_date).birthday_message
    assert expected == actual


def test_birth_date():
    birth_date = datetime.date(1998, 6, 15)
    expected = "It looks like you were born on {}".format(birth_date.strftime("%m/%d/%Y").lstrip('0'))
    actual = BirthdayCalc(birth_date).birth_date_message
    assert expected == actual


def test_message_days_long_past():
    today = datetime.date.today()
    number_of_days = 2
    year = today.year - 46
    two_days = datetime.timedelta(days=number_of_days)
    birth_date = today.replace(year=year) - two_days
    expected = "Looks like your birthday was {} days ago.\nHope you enjoyed your birthday!".format(abs(number_of_days))
    actual = BirthdayCalc(birth_date).birthday_message
    assert expected == actual


def test_message_days_far_future():
    today = datetime.date.today()
    number_of_days = 2
    year = today.year + 9
    two_days = datetime.timedelta(days=number_of_days)
    birth_date = today.replace(year=year) + two_days
    expected = "Looks like your birthday is in {} days.\nHope you're looking forward to it!".format(number_of_days)
    actual = BirthdayCalc(birth_date).birthday_message
    assert expected == actual


def test_message_birthday_years_past():
    today = datetime.date.today()
    year = today.year - 63
    birth_date = today.replace(year=year)
    expected = "HAPPY BIRTHDAY!!"
    actual = BirthdayCalc(birth_date).birthday_message
    assert expected == actual
