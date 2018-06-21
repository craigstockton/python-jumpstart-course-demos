import random

from banner import Banner
from calibrator import Calibrator
from prompt import Prompt


def main():
    print(Banner("GUESS THE NUMBER APP").content)
    calibrator = Calibrator(random.randint(0,100))
    prompt = Prompt()
    success = False
    while not success:
        calibration = calibrator.calibrate(prompt.input())
        print(calibration.message)
        success = calibration.is_equal


if __name__ == "__main__":
    main()
