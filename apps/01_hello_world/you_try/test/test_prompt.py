from hello_world.name_prompt import NamePrompt


def test_prompt():
    expected = "What is your name?"
    actual = NamePrompt().prompt
    assert expected == actual
