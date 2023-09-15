from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """

    try:
        nums = str_with_ints.split()
        nums = [int(num) for num in nums]
        return nums[0] / nums[1]
    except ValueError as m:
        return f'Error code: {m}'
    except ZeroDivisionError as m:
        return f'Error code: {m}'
