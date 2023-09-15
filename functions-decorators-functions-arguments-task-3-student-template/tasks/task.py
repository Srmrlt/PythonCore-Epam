from typing import Dict


def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    result = {}
    for arg in args:
        for key in list(arg):
            if key in list(result):
                result[key] = result[key] + arg[key]
            else:
                result.update({key: arg[key]})

    return result
