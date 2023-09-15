def replacer(s: str) -> str:
    """
    Add your code here
    """
    result = ''
    for char in s:
        if char == '\'':
            result = f'{result}\"'
        elif char == '\"':
            result = f'{result}\''
        else:
            result = f'{result}{char}'
    return result
