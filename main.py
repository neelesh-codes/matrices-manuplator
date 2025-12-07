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

st.sidebar.markdown("""[Go to github](https://github.com/neelesh-codes/matrices-manuplator)""")  # noqa: E501

st.sidebar.subheader("About:")

st.sidebar.markdown("""
### Matrices Manuplator

This is a app created by [neelesh-codes](https://github.com/neelesh-codes) to make matrices operations easy.
Key Points:
- It can work with .npy files.
- Need not to deal with brackets ([...]) again and again.
- Can do multiple operations.
- Array transposing is also supported.
- Availabel as open source on github.
- There will be more but keep this much till now...
""")  # noqa: E501
