import streamlit as st

st.title("streamlit app")

text = st.text_input("write something")

if st.button("show text"):
    st.write(f"you write this {text}")