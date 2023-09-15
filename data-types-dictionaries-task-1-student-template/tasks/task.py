from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here
    s = s.lower()
    s_list = [i for i in s]
    s_list.sort()
    d_list = [(char, s_list.count(char)) for char in s_list]

    return dict(d_list)
