import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

_DEFAULT_TITLE = "Python AI Starter Template"
APP_TITLE = os.environ.get("APP_TITLE", _DEFAULT_TITLE)

st.set_page_config(page_title=APP_TITLE, page_icon="🤖")

st.title(APP_TITLE)
st.write("A minimal starter app for AI-powered Python projects.")
