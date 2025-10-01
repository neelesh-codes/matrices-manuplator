import util1.Numpy_array_manuplator as nam
import numpy as np
import os
import shutil
import sys


class NPY_file_changer(nam):
    def __init__(self, take_args: int = 0):
        self.take_args = take_args

    def load_npy_file(self, npy_file_path: str):
        """This function will load a .npy file and show the data inside it.
        args:
            self: default arguent for object calling.
            npy_filr_path: the path of the .npy file that to load."""
        npy_file = np.load(npy_file_path)
        print(f"The data inside {npy_file_path}: \n{npy_file}")
        print("|| Completed ||x")

    def copy_npy_file(self, src, dest):
        """This function will load a npy file and then copy it to another destination.
        args:
            self: The default argument for object.
            src: source destination that to copy.
            dest: destination where to paste the source file."""
        shutil.copy(src, dest)
        print("Copied successfully!")
        print("here are the results: ")
        file = np.load(dest)
        print(file)
        print("+--------------------+------------------+")

    def basic_info_of_file(self, npy_file_path):
        """This function loads a file and show a basic information of it like minimumm value, maximumm value, data type , size, shape etc.
        args:
            self: default argument for object.
            npy_file_path: The path of the file that to load."""
        print(
            f"We are going to show the basic info of the file:\n{npy_file_path}")
        npy_file: np.array = np.load(npy_file_path)
        print("Loaded file successfully!")
        print("Here is the basic info: ")
        print("+--------------+------------------+")
        print(npy_file)

        print("Here is the basics info: ")
        print(f"Max va;lue{np.max(npy_file)} ")
        print(f"Min Value: {np.min(npy_file)} ")
        print(f"Sum of all numbers of npy array {np.sum(npy_file)} ")
        print(f"The Data Type of the array: {npy_file.dtype} ")
        print(f"The shape of the array is: {npy_file.shape}")
        print(f"The size of the array is: {npy_file.size}")


if __name__ == "__main__":
    pass
