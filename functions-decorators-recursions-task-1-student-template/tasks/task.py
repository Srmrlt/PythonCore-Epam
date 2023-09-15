from typing import List, Tuple, Union
from functools import reduce


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    for seq in sequence:
        if type(seq) == list or type(seq) == tuple:
            sequence.remove(seq)
            sequence.extend(seq)
    print(sequence)

    return reduce(lambda x, y: x + y, sequence, 0)
