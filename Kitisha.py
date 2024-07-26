import streamlit as st

#set the title of the app
st.title("Welcome to my first Streamlit app")

# Add a text inout
name = st.text_input("Enter your name:")

#Display the name entered by the user
if name:
  st.write(f"Hello, {name}! Welcome to the app.")
