from datetime import date


class PromptBirthDate:
    def __init__(self):
        """
        Prompts for a Year, Month and Day assuming it is a Birth Date
        """
        self.prompt_day = "What day were you born [DD]? "
        self.prompt_month = "What month were you born [MM]? "
        self.prompt_year = "What year were you born [YYYY]? "

    def input(self):
        """
        Receive Birth Date input from a user and return it as a datetime
        """
        year = int(input(self.prompt_year))
        month = int(input(self.prompt_month))
        day = int(input(self.prompt_day))
        return date(year, month, day)
