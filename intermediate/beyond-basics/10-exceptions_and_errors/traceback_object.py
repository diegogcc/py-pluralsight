import math
import traceback

class InclinationError(Exception):
    pass

def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e

def main():
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e.__traceback__)          # <traceback object at 0x10a2ae5a0>
        traceback.print_tb(e.__traceback__)
        #   File "traceback_object.py", line 15, in main
        #     inclination(0, 5)
        #   File "traceback_object.py", line 11, in inclination
        #     raise InclinationError("Slope cannot be vertical") from e

        s = traceback.format_tb(e.__traceback__)
        print(s)
        # ['  File "traceback_object.py", line 15, in main\n
        #     inclination(0, 5)\n', 
        # '  File "traceback_object.py", line 11, in inclination\n
        #     raise InclinationError("Slope cannot be vertical") from e\n']


if __name__ == "__main__":
    main()
    print("Finished")                   # Finished