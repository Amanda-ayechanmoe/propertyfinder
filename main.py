import streamlit as st
from extract_data import extract_data
from extract_data99co import extract_data
from upload_searchcriteria_to_S3 import search_param

st.set_page_config()

st.header("Look below this for me")

with st.form(key='filter_form'):
    search_by_MRT = st.multiselect('SELECT ',("East-West Line","North-South Line"))
    user_email = st.text_input("Your email address")
    button = st.form_submit_button()
    if button:
        search_by_MRT.append(user_email)
        search_param(search_by_MRT)
        st.info("We will notify you once we found property you are looking for")
