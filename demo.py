import streamlit as st

# https://github.com/streamlit/release-demos/blob/master/0.65/demos/query_params.py
query_params = st.experimental_get_query_params()
default = query_params["text"][0] if "text" in query_params else ""

x = st.text_area('Enter Text', value=default)

st.write('The text in uppercase is ', x.upper())

