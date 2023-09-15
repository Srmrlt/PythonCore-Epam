from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    '''
    overloading the addition
    List[int] + str = ['int[0] str', 'int[1] str', ... 'int[n] str']
    '''
    def __add__(self, b):
        return [f'{c} {b}' for c in self.values]
