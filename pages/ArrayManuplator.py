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
    arr1 = np.array([
        [int(x) for x in row.replace(" ", "").split(",")]
        for row in rows
    ])

if arr2:
    rows = arr2.strip().split("\n")
    arr2 = np.array([
        [int(x) for x in row.replace(" ", "").split(",")]
        for row in rows
    ])

if add:
    st.write("After the array is added: ")
    summed_arrays = array_model.add_two_arrays(arr1, arr2)
    st.write(summed_arrays)

if sub:
    st.write("After the array is subtracted: ")
    subtracted_array = array_model.subtract_two_arrays(arr1, arr2)
    st.write(subtracted_array)

if mul:
    st.write("After the array is subtracted: ")
    producted_array = array_model.multiply_two_arrays(arr1, arr2)
    st.write(producted_array)

if div:
    st.write("After the array is subtracted: ")
    quointed_array = array_model.divide_two_arrays(arr1, arr2)
    st.write(quointed_array)

st.markdown("---")

st.header("Transpose your array here")

array = st.text_area("Enter the array here: ")

if not array:
    st.error("Array is empty!")

if array:
    rows = array.strip().split("\n")
    array = np.array([
        [int(x) for x in row.replace(" ", "").split(",")]
        for row in rows
    ])

trans = st.button("Transpose the array: ")

if trans:
    transposed_array = array_model.transpose_the_array(array)
    st.write("After the array is transpoed: ")
    st.write(transposed_array)

st.markdown("---")

st.header("Thank You! for comming till here!")

