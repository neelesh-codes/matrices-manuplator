import numpy as np
import pandas as pd
import streamlit as st
import pyttsx3
from utils.util1 import Numpy_array_manipulator
from utils.util2 import NPY_file_changer

engine = pyttsx3.init()

st.title("Welcome to - Matrices Manuplator!")

data = st.text_area("Enter array values")

speak = st.checkbox('Want us to dectate results for you?')
if data:
    # split into rows
    rows = data.strip().split("\n")
    # convert each row into integers
    arr = np.array([
        [int(x) for x in row.replace(" ", "").split(",")]
        for row in rows
    ])

    st.subheader("Info of matrices (array)")
    st.write(arr)
    st.write("Shape:", arr.shape)
    st.write("Dtype:", arr.dtype)
    st.write("Size:", arr.size)
    st.write("Item size", arr.itemsize)

if speak:
    engine.say(f"Shape: {arr.shape}")
    engine.say("Dtype: {}".format(arr.dtype))
    engine.say("Size: {}".format(arr.size))
    engine.say("Item size {}".format(arr.itemsize))
    engine.runAndWait()