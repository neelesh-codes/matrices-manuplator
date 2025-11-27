# All the modules needed:
from utils.util2 import NPY_file_changer
import numpy as np
import streamlit as st
import pyttsx3

# In pages/page1.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


menuplator = NPY_file_changer()

import streamlit as st
import pyttsx3

# Initialize engine in session state
if 'tts_engine' not in st.session_state:
    st.session_state.tts_engine = pyttsx3.init()

def speak_text(text):
    engine = st.session_state.tts_engine
    engine.say(text)
    # Don't call runAndWait() here

# Your file processing code


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
