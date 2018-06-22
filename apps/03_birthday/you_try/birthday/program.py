from birthday_calc import BirthdayCalc
from prompt_birth_date import PromptBirthDate

birth_date = BirthdayCalc(PromptBirthDate().input())
print()
print(birth_date.birth_date_message)
print(birth_date.birthday_message)
