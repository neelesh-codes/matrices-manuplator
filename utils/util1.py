import numpy as np
import datetime
import os
import shutil
import pyttsx3
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


class Numpy_array_manuplator:
    def __init__(self, like_this: int = 0):
        """
        An empty constructor.
        """
        # self.__nfoa = npy_file_or_array
        self.like_this = like_this
    # No need of constructer till now.

    def basic_info(self, arr, speak_also=False) -> np.array:
        """
        The function takes one argument "speak_also" asking programmer the permissing that is programm ought to speak it.

        It gives the basics info of the array like maximumm value, minimumm value, sum of all value and datatype of the array.

        The function can speak all the information about the array if permitted to use microphone.
        """
        npy_array: np.array = arr
        print(f"Max value: {np.max(npy_array)} ")
        print(f"Min Value: {np.min(npy_array)} ")
        print(f"Sum of all numbers of npy array {np.sum(npy_array)} ")
        print(f"The Data Type of the array: {npy_array.dtype} ")
        print(f"The shape of the array is: {npy_array.shape}")
        print(f"The size of the array is: {npy_array.size}")
        time.sleep(3)
        if speak_also == True:

            engine.say(f"Max value: {np.max(npy_array)} ")
            engine.say(f"Min Value: {np.min(npy_array)} ")
            engine.say(f"Sum of all numbers of npy array {np.sum(npy_array)} ")
            engine.say(f"The Data Type of the array: {npy_array.dtype} ")
            engine.say(f"Work completed at {datetime.datetime.now()}")
            engine.runAndWait()
            engine.say(f"The shape of the array is: {npy_array.shape}")
            engine.say(f"The size of the array is: {npy_array.size}")
        return npy_array

    def multply_two_arrays(self, array_1, array_2, speak_also=False):
        """
        The function will return the mutliplied product of two arrays
        args:
            Fucntion takes two argument and one default argumemt "self" and two arguments "array_1" and "array_2" and return product of both of the arrays.
        """
        result = array_1 @ array_2
        print(f"Product of the function is: {result}")
        return result

        if speak_also == True:
            engine.say(f"Product of the function is: {result}")


if __name__ == "__main__":
    print("Hello I am Neelesh")
    Instance = Numpy_array_manuplator()
    arr = np.linspace(1, 20, 13, endpoint=True, dtype=np.int32)
    print(arr)
    print()
    # print(Instance.basic_info(arr, speak_also=True))
    arr2 = np.linspace(1, 20, 13, endpoint=True, dtype=np.int32)
    print(Instance.multply_two_arrays(arr, arr2, speak_also=True))
