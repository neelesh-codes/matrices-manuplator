import numpy as np
# import pandas as pd
import streamlit as st
# from utils.util1 import Numpy_array_manipulator
# from utils.util2 import NPY_file_changer


st.title("Welcome to - Matrices Manuplator!")

data = st.text_area("Enter array values")

if data:
    # split into rows
    rows = data.strip().split("\n")
    # convert each row into integers
    arr = np.array([
        [int(x) for x in row.replace(" ", "").split(",")]
        for row in rows
    ])

if not data:
    st.error("Aray is empty")

if data:
    st.subheader("Info of matrices (array)")
    st.write(arr)
    st.write("Shape:", arr.shape)
    st.write("Dtype:", arr.dtype)
    st.write("Size:", arr.size)
    st.write("Item size", arr.itemsize)
