from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    # TODO: Add your code here
    result = []
    for word in str_list:
        if word not in result:
            result.append(word)
    result.sort()
    return result
