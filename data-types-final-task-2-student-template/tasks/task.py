from typing import List


def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """
    row = [i for i in range(row_start, row_end + 1)]
    column = [i for i in range(column_start, column_end + 1)]
    mult_table = [[r * c for c in column] for r in row]

    table = ' ' * 5
    for c in range(len(column)):
        table = f'{table} {column[c]:3} '
    table = f'{table}\n'
    for r in range(len(row)):
        table = f'{table} {row[r]:3} '
        for c in range(len(column)):
            table = f'{table} {mult_table[r][c]:3} '
        table = f'{table}\n'
    print(table)

    return mult_table
