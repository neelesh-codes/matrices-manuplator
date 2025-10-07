from . import util1
import numpy as np
import os
import shutil
import sys
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


class NPY_file_changer(util1.Numpy_array_manipulator):
    def __init__(self, take_args: int = 0):
        super().__init__()
        self.take_args = take_args

    def load_npy_file(self, npy_file_path: str):
        """This function will load a .npy file and show the data inside it.
        args:
            self: default argument for object calling.
            npy_file_path: the path of the .npy file that to load."""
        npy_file = np.load(npy_file_path)
        print(f"The data inside {npy_file_path}: \n{npy_file}")
        print("|| Completed ||")
        return npy_file

    def copy_npy_file(self, src, dest):
        """This function will load a npy file and then copy it to another destination.
        args:
            self: The default argument for object.
            src: source destination that to copy.
            dest: destination where to paste the source file."""
        shutil.copy(src, dest)
        print("Copied successfully!")
        print("Here are the results: ")
        file = np.load(dest)
        print(file)
        print("+--------------------+------------------+")
        return file

    def basic_info_of_file(self, npy_file_path, speak_also: bool = False):
        """This function loads a file and show a basic information of it like minimum value, maximum value, data type, size, shape etc.
        args:
            self: default argument for object.
            npy_file_path: The path of the file that to load."""
        print(f"We are going to show the basic info of the file:\n{npy_file_path}")
        npy_file: np.array = np.load(npy_file_path, allow_pickle=True)
        print("Loaded file successfully!")
        print("Here is the basic info: ")
        print("+--------------+------------------+")
        print(npy_file)

        info = []
        info.append(f"Max value: {np.max(npy_file)}")
        info.append(f"Min Value: {np.min(npy_file)}")
        info.append(f"Sum of all numbers of npy array: {np.sum(npy_file)}")
        info.append(f"The Data Type of the array: {npy_file.dtype}")
        info.append(f"The shape of the array is: {npy_file.shape}")
        info.append(f"The size of the array is: {npy_file.size}")

        print("Here is the basic info: ")
        for line in info:
            print(line)

        if speak_also == True:
            for line in info:
                engine.say(line)
                engine.runAndWait()
        
        return npy_file

    def move_to_npy(self, data: np.array, file_path: str):
        """This function converts a array or a group of arrays into a .npy file.
        args:
            self: default argument for object.
            data: The data to store in the npy file.
            file_path: name of the .npy file in which data to be stored."""
        np.save(file_path, data)
        print(f"Saved the data to {file_path}.")
        print("The data is: ")
        file_data = np.load(file_path)
        print(file_data)
        return file_data


if __name__ == "__main__":
    try:
        instance = NPY_file_changer()
        # Update this path to your actual test file path
        test_file = "test_array.npy"
        
        # Create a test file if it doesn't exist
        if not os.path.exists(test_file):
            test_data = np.array([[1, 2, 3], [4, 5, 6]])
            np.save(test_file, test_data)
            print(f"Created test file: {test_file}")
        
        instance.basic_info_of_file(test_file)
        
    except Exception as e:
        print(f"The error is: {e}")
    else:
        print("Passed successfully.")
    finally:
        print('Exiting the program!')