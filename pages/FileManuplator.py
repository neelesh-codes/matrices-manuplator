# All the modules needed:
from utils.util2 import NPY_file_changer
import numpy as np
import pandas as pd
import streamlit as st

# In pages/page1.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


menuplator = NPY_file_changer()


# title of the file
st.title("Manuplate NPY files")

# This variable holds file_path
file_path = st.text_input("Enter the file path: ")

# The button that asks from user wheather to see data or not
see_data = st.button("See data of file")

# code that to be exccuted when user will click on see_data
if see_data:
    file_data = menuplator.load_npy_file(file_path)
    st.subheader("Here is the data")
    st.write(file_data)

# Below section show basic info of file
st.subheader("See basic info of file here")

# This checkbox asks for shwoing the info of file or not
see_info = st.checkbox('Show all info')

# Below code will be excecuted when see_info will be selected
if see_info:
    if file_path == "":
        st.error("No file selected")
    st.write(pd.DataFrame(menuplator.basic_info_of_file(file_path)))
    st.success("Shown all informarion that we have")

# below script will copy the source file to destination file.
st.subheader("Copy a npy file to another")

# Some instructions for user.
st.text("Note: The source file will be the first file that you added in above input box!")  # noqa: E501

# destination file path
destination = st.text_input("Enter the destination path")

# The button which will ask for copying the file
copy = st.button("Copy now")

# below script will excecute when copy button will be clicked
if copy:
    menuplator.copy_npy_file(file_path, destination)
    st.success('Copied successfully!')

st.subheader('Convert a goroup of numbers to npy file from here')

array = st.text_area("Enter the array here.")
rows = array.strip().split("\n")
data = np.array([
    [int(x) for x in row.replace(" ", "").split(",") if x != '']
    for row in rows
    if row.strip() != ''  # Also skip empty rows
])


if array:
    st.write("Here is the array: ")
    st.write(data)

new_file_path = st.text_input('Enter the path of new file')
move = st.button("Move to .npy file")

if move:
    menuplator.move_to_npy(data, new_file_path)
    st.success("Moved successfully!")

st.markdown("---")

st.header("Thank You! for comming till here!")
