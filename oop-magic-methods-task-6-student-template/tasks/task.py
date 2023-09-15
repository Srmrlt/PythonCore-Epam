import os


class Cd:
    def __init__(self, path: str):
        self.home_path = os.getcwd()

        if path[0] == '/':
            path = path[1:]
        self.dir_name = path
        directory = os.path.join(self.home_path, self.dir_name)
        directory_2dot = os.path.join(self.home_path, os.pardir, self.dir_name)
        self.new_path = os.path.abspath(directory)
        self.new_path_2dot = os.path.abspath(directory_2dot)

    def __enter__(self):
        if os.path.isdir(self.new_path):
            os.chdir(self.new_path)
        elif os.path.isdir(self.new_path_2dot):
            os.chdir(self.new_path_2dot)
        else:
            raise ValueError

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.home_path)
