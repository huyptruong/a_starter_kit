import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

APP_TITLE = os.getenv("APP_TITLE", "Python AI Starter Template")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


@st.cache_data(show_spinner=False)
def fetch_reply(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Set OPENAI_API_KEY in `.env` (see `.env.example`).")
    client = OpenAI(api_key=api_key)
    r = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return r.choices[0].message.content or ""


st.set_page_config(page_title=APP_TITLE, layout="centered")
st.title(APP_TITLE)

if "reply" not in st.session_state:
    st.session_state.reply = ""

prompt = st.text_area("Your prompt", height=150, placeholder="Enter your question here…")

if st.button("Submit"):
    text = prompt.strip()
    if not text:
        st.error("Please enter a prompt before submitting.")
    else:
        try:
            with st.spinner("Generating response…"):
                st.session_state.reply = fetch_reply(text)
        except Exception as exc:
            st.error(str(exc))

st.text_area("Response", value=st.session_state.reply, height=240, disabled=True)
