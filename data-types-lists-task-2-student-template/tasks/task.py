from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    # TODO: Add your code here
    result = []
    for i in range(1, n + 1):
        if (not i % 3) and (not i % 5):
            result.append('FizzBuzz')
        elif not i % 3:
            result.append('Fizz')
        elif not i % 5:
            result.append('Buzz')
        else:
            result.append(i)
    return result
