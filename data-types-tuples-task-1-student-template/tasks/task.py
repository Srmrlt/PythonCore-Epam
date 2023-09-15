from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    # TODO: Add your code here
    num_list = [int(i) for i in str(num)]
    return tuple(num_list)
