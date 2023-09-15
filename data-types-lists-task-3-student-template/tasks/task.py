from typing import List
import math


def foo(nums: List[int]) -> List[int]:
    # TODO: Add your code here
    result = [int(math.prod(nums) / i) for i in nums if i]
    return result
