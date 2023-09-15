class Cipher:
    _alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()

    def __init__(self, key: str):
        key = list(key.upper())
        cipher_alphabet = []
        for v in (key + self._alphabet):
            if v not in cipher_alphabet:
                cipher_alphabet.append(v)
        self._cipher_alphabet = cipher_alphabet

    def encode(self, data: str):
        return self.encrypting(data, self._alphabet, self._cipher_alphabet)
    
    def decode(self, data: str):
        return self.encrypting(data, self._cipher_alphabet, self._alphabet)

    @staticmethod
    def encrypting(data: str, alphabet_in: list, alphabet_out: list):
        data_encrypted = ''
        alphabet_in_low = list(map(str.lower, alphabet_in))
        alphabet_out_low = list(map(str.lower, alphabet_out))
        for char in data:
            if char in alphabet_in:
                data_encrypted += alphabet_out[alphabet_in.index(char)]
            elif char in alphabet_in_low:
                data_encrypted += alphabet_out_low[alphabet_in_low.index(char)]
            else:
                data_encrypted += char
        return data_encrypted
