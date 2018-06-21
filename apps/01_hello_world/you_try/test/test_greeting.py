from hello_world.greeting import Greeting


def test_greet():
    name = "Craig"
    expected = "Nice to meet you {}".format(name)
    actual = Greeting(name).greet()
    assert expected == actual
