from journal import Journal
from menu import Menu


def main():
    journal = Journal()
    menu = Menu()
    selection = menu.prompt()
    while selection != 'x':
        if selection == 'l':
            print(journal.list())
        elif selection == 'a':
            journal.add(input('Enter your journal entry:\n'))
        selection = menu.prompt()
    journal.save()


if __name__ == '__main__':
    main()
