from typing import List


def split(data: str, sep=None, maxsplit=-1) -> List:
    if sep is None:
        sep = ('\n', '\r', '\t', '\f', ' ')
        emp = True
    else:
        emp = False

    list_data = list()
    list_data.append(data)

    result = rec(list_data, sep, emp, maxsplit)

    return result


def rec(data: list, separator, emp: bool, sp: int):
    if emp:
        data[0] = data[0].lstrip()
        sep = sep_find(data[-1], separator)
        while data[-1].find(sep) == 0:
            data[-1] = data[-1].lstrip(sep)
            sep = sep_find(data[-1], separator)
    else:
        sep = separator
    not_last = data[-1].find(sep) + 1
    if (len(data) != sp+1) and not_last:
        d = list(data[-1].partition(sep))
        d.remove(sep)
        data.remove(data[-1])
        data += d
        if emp:
            while '' in data:
                data.remove('')
        rec(data, separator, emp, sp)
    elif emp:
        while '' in data:
            data.remove('')
    return data


def sep_find(data: str, sep):
    sep_index = 4
    s_index = len(data) - 1
    for i, s in enumerate(sep):
        if (s in data) and (data.find(s) <= s_index):
            s_index = data.find(s)
            sep_index = i
    return sep[sep_index]
