from hello_world.banner import Banner


def test_content():
    line = "".ljust(33, "-")
    message = "HELLO APP"
    banner_message = message.rjust(15, " ")
    expected = "{}\r\n{}\r\n{}\r\n".format(line, banner_message, line)
    print(expected)
    actual = Banner(message).content
    assert expected == actual
