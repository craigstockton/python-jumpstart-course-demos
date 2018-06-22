import datetime


class BirthdayCalc:
    def __init__(self, birth_date):
        """
        Provides information about an assumed Birth Date, such as how many day since or until this year's Birthday
        """
        future_message = "Looks like your birthday is in {}.\nHope you're looking forward to it!"
        past_message = "Looks like your birthday was {} ago.\nHope you enjoyed your birthday!"
        birthday_message = "HAPPY BIRTHDAY!!"
        birth_date_message_format = "It looks like you were born on {}"
        today = datetime.date.today()
        self.birth_date_message = birth_date_message_format.format(birth_date.strftime("%m/%d/%Y").lstrip('0'))
        diff = (birth_date.replace(year=today.year) - today).days
        if diff > 0:
            self.birthday_message = future_message.format(
                "{} day".format(diff) if diff == 1 else "{} days".format(diff))
        elif diff < 0:
            diff = abs(diff)
            self.birthday_message = past_message.format("{} day".format(diff) if diff == 1 else "{} days".format(diff))
        else:
            self.birthday_message = birthday_message
