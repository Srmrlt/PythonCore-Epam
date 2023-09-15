from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # TODO: Add your code here
    result = []
    for i in range(1, len(lst)):
        result.append((lst[i - 1], lst[i]))
    return result
