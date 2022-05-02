class AbsException(Exception):
    pass


def read_input_float(prompt: str = "Input a float value: ") -> float:
    """Reads a float from user input

    Args:
        prompt (str, optional): user prompt. Defaults to "Input a float value: ".

    Raises:
        AbsException: can't convern input string to float

    Returns:
        float: resulting float
    """
    try:
        return float(input(prompt))
    except (TypeError, ValueError, EOFError) as e:
        raise AbsException(
            f"Can't validate your input as the float number: {str(e)}")


def calculate(x: float, y: float) -> float:
    """Returns an abs between `x` and `y`

    Args:
        x (float): the first number
        y (float): the second number

    Returns:
        float: an abs between `x` and `y`
    """
    return abs(x - y)


if __name__ == '__main__':
    try:
        x = read_input_float("Type in `x` value, please: ")
        y = read_input_float("Type in `y` value, please: ")
        print(f"The length between `x` and `y` is {calculate(x, y)}")
    except AbsException as e:
        print(str(e))
