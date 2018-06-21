from hello_world.banner import Banner


def test_content():
    line = "".ljust(33, "-")
    banner_message = "HELLO APP".rjust(15, " ")
    expected = "{}\r\n{}\r\n{}\r\n".format(line, banner_message, line)
    print(expected)
    actual = Banner().content
    assert expected == actual
