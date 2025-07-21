import streamlit as st
import pandas as pd

# Load winner data
df = pd.read_csv('winners.csv')

# UI
st.title("AEON Charity Run 2025 - Lucky Draw Checker")
bib = st.text_input("Enter your Bib Number")

if st.button("Check Result"):
    result = df[df['Bib Number'] == bib.upper()]
    if not result.empty:
        name = result.iloc[0]['Name']
        prize = result.iloc[0]['Prize']
        st.success(f"🎉 Congratulations {name}! You've won a {prize}!")
    else:
        st.error("Sorry, you're not on the winner list.")
