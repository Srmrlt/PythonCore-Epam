from typing import Any, List


def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    for seq in sequence:
        if type(seq) == list or type(seq) == tuple:
            sequence.remove(seq)
            sequence.extend(seq)
            linear_seq(sequence)
    return sequence
