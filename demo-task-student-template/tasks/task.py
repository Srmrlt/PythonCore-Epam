from typing import Tuple, Union
from math import sqrt


def solution(a, b, c) -> Union[Tuple[float, float], Tuple[float], None]:
    # Add your code here or call it from here  
    result = tuple()
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        result = (-b - sqrt(discriminant)) / (2 * a), (-b + sqrt(discriminant)) / (2 * a)
    elif discriminant == 0:
        result = -b / (2 * a),
    else:
        result = None
    print(result)
    return result 
