def union(*args) -> set:
    result = set()
    for arg in args:
        result = result.union(arg)
    return result


def intersect(*args) -> set:
    result = set(args[0])
    for arg in args:
        result = result.intersection(arg)
    return result
