from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    i_start = 0
    result_list = []
    for i in range(len(s)):
        if i in indexes:
            result_list.append(s[i_start:i])
            i_start = i
    result_list.append(s[i_start:])
    return result_list
