def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here  
    """
    a = int(a_b.split('/')[0])
    c = int(c_b.split('/')[0])
    b1 = a_b.split('/')[1]
    b2 = c_b.split('/')[1]
    if b1 == b2:
        result = f'{a_b} + {c_b} = {a + c}/{b1}'
    else:
        result = f'Error'
    return result
