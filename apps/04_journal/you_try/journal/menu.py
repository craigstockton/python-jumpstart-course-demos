class Menu:
    """
    Display journal menu and prompt for user's selection.
    """
    prompt_message = "What do you want to do? [L]ist, [A]dd, e[X]it? "

    def prompt(self):
        """
        Prompt user for menu selections on console.  Invalid entries re-prompt for input.

        :return: User's menu selection (l, a or x)
        """
        user_input = input(self.prompt_message).lower().strip()
        while user_input not in {'l', 'a', 'x'}:
            user_input = input(self.prompt_message).lower().strip()
        return user_input
