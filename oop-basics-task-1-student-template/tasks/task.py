class Field:
    __value = None

    def __init__(self):
        self.__value = None

    def set_value(self, new):
        self.__value = new

    def get_value(self):
        return self.__value
