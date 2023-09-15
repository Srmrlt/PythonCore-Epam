def get_longest_word(s: str) -> str:
    """
     Add your code here 
    """
    word_length = 0
    longest_word = ''
    for word in s.split():
        if len(word) > word_length:
            word_length = len(word)
            longest_word = word
    return longest_word
