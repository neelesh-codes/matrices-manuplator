import util1.Numpy_array_manuplator as nam
import numpy as np
import os
import shutil

class NPY_file_changer(nam):
    def __init__(self, take_args: int=0):
        self.take_args = take_args

    def load_npy_file(self, npy_file_path: str):
        npy_file = np.load(npy_file_path)
        print(f"The data inside {npy_file_path}: \n{npy_file}")
        print("|| Completed ||x")

if __name__ == "__main__":
    pass