from utils.util1 import Numpy_array_manipulator
import numpy as np
import streamlit as st
import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


array_model = Numpy_array_manipulator()

st.title("Do array operations here!")
st.markdown("---")

st.header("Get basic info of a array")

data = st.text_area("Enter array values")

if not data:
    st.error("Array is empty")

if data:
    # split into rows
    rows = data.strip().split("\n")
    # convert each row into integers
    arr = np.array([
        [int(x) for x in row.replace(" ", "").split(",")]
        for row in rows
    ])

get_info = st.button("Get the info!")

if get_info:
    with st.spinner("Wait for some itme"):
        time.sleep(3)
        st.dataframe(array_model.basic_info(arr))
        st.success("Shown all info")

del data
st.markdown("---")

st.header("Operations on arrays")

arr1 = st.text_area("Enter the first array: ")
col1, col2, col3 = st.columns(3)

add = st.button("add")
sub = st.button("subtract")
mul = st.button("multiply")
div = st.button("devide")
arr2 = st.text_area("Enter the second array: ")


if not arr1 and arr2:
    st.error("Array bot array are empty")

if arr1:
    rows = arr1.strip().split("\n")
    arr = np.array([
        [int(x) for x in row.replace(" ", "").split(",")]
        for row in rows
    ])

if arr2:
    rows = arr2.strip().split("\n")
    arr = np.array([
        [int(x) for x in row.replace(" ", "").split(",")]
        for row in rows
    ])
