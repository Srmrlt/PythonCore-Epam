from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    """
    Add your code here or call it from here   
    """
    square_dict = {x: x ** 2 for x in range(1, num + 1)}

    return square_dict
