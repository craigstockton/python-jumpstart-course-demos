class Banner:
    def __init__(self):
        line_separator = "".ljust(33, "-")
        banner_message = "HELLO APP"
        padding_size = 6
        message_line = banner_message.rjust(banner_message.__len__()+padding_size, " ")
        self.content = "{}\r\n{}\r\n{}\r\n".format(line_separator, message_line, line_separator)
