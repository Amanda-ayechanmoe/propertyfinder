import streamlit as st
from extract_data import extract_data
from extract_data99co import extract_data

st.set_page_config()

st.header("Look below this for me")

with st.form(key='filter_form'):
    search_by_MRT = st.multiselect('SELECT one',("East-West Line","North-South Line"))
    button = st.form_submit_button()
    if button:
        extract_data()
