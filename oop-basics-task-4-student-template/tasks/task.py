class HistoryDict:
    def __init__(self, new_dict):
        self.my_dict = new_dict
        self.my_dict = {}

    def set_value(self, key, value):
        if key in self.my_dict:
            self.my_dict.pop(key)
        if len(self.my_dict) >= 5:
            key_list = list(self.my_dict.keys())
            self.my_dict.pop(key_list[0])

        self.my_dict[key] = value

    def get_history(self):
        key_list = list(self.my_dict.keys())
        return key_list
