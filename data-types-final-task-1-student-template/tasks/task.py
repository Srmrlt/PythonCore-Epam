from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    val_list = [val for dicts in lst for val in dicts.values()]

    return set(val_list)
