from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    cur = ''
    cur_rate = {'EUR2USD': 2.0,
                'EUR2GBP': 100.0,
                'EUR2EUR': 1.0,
                'USD2EUR': 0.5,
                'USD2GBP': 50.0,
                'USD2USD': 1.0,
                'GBP2EUR': 0.01,
                'GBP2USD': 0.02,
                'GBP2GBP': 1.0
                }

    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f'{self.value} {self.cur}'

    def __add__(self, other_cls):
        class_name = self.__class__
        add_part = self.convert(other_cls)
        return class_name(self.value + add_part)

    def __gt__(self, other_cls):
        value = self.convert(other_cls)
        return self.value > value

    def __lt__(self, other_cls):
        value = self.convert(other_cls)
        return self.value < value

    def __eq__(self, other_cls):
        value = self.convert(other_cls)
        return self.value == value

    def convert(self, other_cls):
        class_name = self.__class__  # Getting the class name of currency to convert
        currency = other_cls.to_currency(class_name)  # Creating new object with converting currency
        value = currency.__str__()  # string {value} {currency name}
        value = float(value[:-4])  # converting value to float
        return value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        rate = cls.cur_rate[f'{cls.cur}2{other_cls.cur}']
        return f'{rate} {other_cls.cur} for 1 {cls.cur}'

    def to_currency(self, other_cls: Type[Currency]):
        rate = self.cur_rate[f'{self.cur}2{other_cls.cur}']
        return other_cls(self.value * rate)


class Euro(Currency):
    cur = 'EUR'


class Dollar(Currency):
    cur = 'USD'


class Pound(Currency):
    cur = 'GBP'
