import re


def check_str(s: str):
    """
    Add your code here
    """
    palindrome = True
    symbol_del = re.sub(r'\W', '', s)
    lower_letter = symbol_del.lower()
    for i in range(len(lower_letter)):
        revers_i = i * (-1) - 1
        if lower_letter[i] != lower_letter[revers_i]:
            palindrome = False
            break

    return palindrome
