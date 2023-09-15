import os
import shutil
from random import random


class TempDir:
    def __init__(self):
        self.dir_name = TempDir.rand_name()
        self.home_path = os.getcwd()

    def __enter__(self):
        os.mkdir(self.dir_name)
        self.new_path = os.path.abspath(self.dir_name)
        os.chdir(self.new_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.home_path)
        shutil.rmtree(self.new_path)

    @staticmethod
    def rand_name():
        return str(hash(random()))
