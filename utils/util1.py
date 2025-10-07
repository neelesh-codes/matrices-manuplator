import numpy as np
import datetime
import os
import shutil
import pyttsx3
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


class Numpy_array_manipulator:
    def __init__(self, like_this: int = 0):
        """
        An empty constructor.
        """
        self.like_this = like_this

    def basic_info(self, arr, speak_also=False) -> np.array:
        """
        The function takes one argument "speak_also" asking programmer the permission that is program ought to speak it.

        It gives the basic info of the array like maximum value, minimum value, sum of all value and datatype of the array.

        The function can speak all the information about the array if permitted to use microphone.
        """
        npy_array: np.array = arr
        info = []
        info.append(f"Max value: {np.max(npy_array)}")
        info.append(f"Min Value: {np.min(npy_array)}")
        info.append(f"Sum of all numbers of npy array: {np.sum(npy_array)}")
        info.append(f"The Data Type of the array: {npy_array.dtype}")
        info.append(f"The shape of the array is: {npy_array.shape}")
        info.append(f"The size of the array is: {npy_array.size}")
        
        for line in info:
            print(line)
        
        time.sleep(0.5)
        if speak_also == True:
            for line in info:
                engine.say(line)
                engine.runAndWait()
            engine.say(f"Work completed at {datetime.datetime.now()}")
            engine.runAndWait()
        
        return npy_array

    def multiply_two_arrays(self, array_1, array_2, speak_also=False):
        """
        The function will return the multiplied product of two arrays
        args:
            Function takes two argument and one default argument "self" and two arguments "array_1" and "array_2" and return product of both of the arrays.
        """
        result = array_1 @ array_2
        print(f"Product of the function is: {result}")

        if speak_also == True:
            engine.say(f"Product of the function is: {result}")
            engine.runAndWait()
        return result

    def add_two_arrays(self, array_1, array_2, speak_also=False):
        """
        The function takes two arrays: array1 and array2 and return the sum of both arrays.
        args:
            self: A default argument for the object.
            array_1: The first array or path to that array
            array_2: The second array or path to that array
        """
        result = np.add(array_1, array_2)
        print(f"The sum is: {result}")
        if speak_also == True:
            engine.say(f"The result is {result}")
            engine.runAndWait()
        return result

    def subtract_two_arrays(self, array_1, array_2, speak_also=False):
        """
        The function takes two arrays: array1 and array2 and return the difference of both arrays.
        args:
            self: A default argument for the object.
            array_1: The first array or path to that array
            array_2: The second array or path to that array
        """
        result = array_1 - array_2
        print(f"The difference is: {result}")
        if speak_also == True:
            engine.say(f"The result is {result}")
            engine.runAndWait()
        return result

    def divide_two_arrays(self, array_1, array_2, speak_also=False):
        """
        The function takes two arrays: array1 and array2 and return the quotient of both arrays.
        args:
            self: A default argument for the object.
            array_1: The first array or path to that array
            array_2: The second array or path to that array
        """
        result = array_1 / array_2
        print(f"The quotient is: {result}")
        if speak_also == True:
            engine.say(f"The result is {result}")
            engine.runAndWait()

        return result

    def transpose_the_array(self, array_to_transpose: np.array, speak_also: bool = False) -> np.array:
        """
        This function will take an array and return the transposing array of it i.e. it will make the rows columns and columns rows respectively.
        args:
            self: default argument for object
            array_to_transpose: the array that will be transposed.
            speak_also: for taking permission to use speakers.
        """
        arr = array_to_transpose
        print(f"Array before transposing: {array_to_transpose}")
        result = arr.T
        print(f"After transposing: {result}")
        if speak_also == True:
            engine.say(f"Array after transposing: {result}")
            engine.runAndWait()
        return result


if __name__ == "__main__":
    print("Hello I am Neelesh")
    Instance = Numpy_array_manipulator()
    arr = np.linspace(1, 20, 13, endpoint=True, dtype=np.int32)
    print(arr)
    print()
    arr2 = np.linspace(1, 20, 13, endpoint=True, dtype=np.int32)
    print(Instance.multiply_two_arrays(arr, arr2, speak_also=True))
    Instance.basic_info(np.array([[1, 2, 3], [4, 5, 6]]), speak_also=True)