import streamlit as st
import pandas as pd
import numpy as np

st.header("Welcome to Dice Key!")

keys = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
modes = ['major', 'minor']
time_signatures = ['2/4', '3/4', '4/4', '5/4', '6/8']
tempos = range(50, 170)
chord_counts = range(1, 10)
genres = ['rock', 'blues', 'classical', 'reggae', 'country']
st.write("Roll the dice to generate new song characteristics:")
if st.button("Roll the dice"):
    key = np.random.choice(keys)
    mode = np.random.choice(modes)
    time_signature = np.random.choice(time_signatures)
    tempo = np.random.choice(tempos)
    chord_count = np.random.choice(chord_counts)
    genre = np.random.choice(genres)
    st.subheader("Your challenge is to write a:")
    st.write(f"**{genre} song** with")
    st.write(f"**{chord_count} chord(s)** in the key of") 
    st.write(f"**{key} {mode}** with a")
    st.write(f"**{time_signature} time signature** at") 
    st.write(f"**{tempo} bpm**.")
    st.subheader("Good Luck!")
    st.write("...or roll the dice again")


