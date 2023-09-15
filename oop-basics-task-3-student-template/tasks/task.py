class Counter:
    def __init__(self, start=0, stop=None):
        self.value = start
        self.value_stop = stop

    def increment(self):
        if (self.value_stop is not None) and (self.value >= self.value_stop):
            print('The maximal value is reached.')
        else:
            self.value += 1

    def get(self):
        return self.value
