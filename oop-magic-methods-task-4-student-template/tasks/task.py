class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __init__(self):
        self.__value = None

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if value > 100 or value < 0:
            raise ValueError('Price must be between 0 and 100.')
        else:
            self.__value = value


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __init__(self, name):
        self.__value = None
        self.__name = name

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if self.__value is None:
            self.__value = value
        else:
            raise ValueError(f'{self.__name} can not be changed.')


class Book:
    author = NameControl('Author')
    name = NameControl('Name')
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
