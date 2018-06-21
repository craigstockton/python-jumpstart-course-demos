from number_guess.prompt import Prompt


def test_prompt_message():
    expected = "Guess a number between 0 and 100: "
    actual = Prompt().message
    assert expected == actual
