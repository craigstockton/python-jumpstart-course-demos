from banner import Banner
from greeting import Greeting
from name_prompt import NamePrompt


def main():
    print(Banner().content)
    print(Greeting(NamePrompt().input()).greet())


if __name__ == "__main__":
    main()
