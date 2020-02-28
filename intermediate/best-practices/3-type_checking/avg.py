"""
Make python use static typing

For VSCODE -> use mypy as linter

"""


def average_dynamic(a, b, c):
    return (a + b + c) / 3


def average_static(a: int, b: int, c: int) -> float:
    """
    Specified parameter's types and return value
    """
    return (a + b + c) / 3


if __name__ == "__main__":
    # Dynamic typing: Runs
    try:
        avgd = average_dynamic(1, 2, "three")
        print(avgd)
    except TypeError:
        print('Wrong parameter type, expected "int".')

    # Static typing: Launches a warning
    try:
        avgs:float = average_static(1, 2, "three")
        print(avgs)
    except TypeError:
        print('Wrong parameter type, expected "int".')
    