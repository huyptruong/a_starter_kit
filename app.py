import streamlit as st
from openai import OpenAI

from config import (
    APP_TITLE,
    MAX_INPUT_CHARS,
    MAX_OUTPUT_TOKENS,
    MAX_REQUESTS_PER_SESSION,
    OPENAI_API_KEY,
    OPENAI_MODEL,
)


@st.cache_data(show_spinner=False)
def fetch_reply(prompt: str) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("Set OPENAI_API_KEY in `.env` (see `.env.example`).")
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
        max_output_tokens=MAX_OUTPUT_TOKENS,
    )
    return response.output_text or ""

st.set_page_config(page_title=APP_TITLE, layout="centered")
st.title(APP_TITLE)

if "request_count" not in st.session_state:
    st.session_state.request_count = 0
if "reply" not in st.session_state:
    st.session_state.reply = ""

prompt = st.text_area("Your prompt", height=150, placeholder="Enter your question here…")
remaining_requests = MAX_REQUESTS_PER_SESSION - st.session_state.request_count
st.caption(f"Remaining requests: {remaining_requests}")

if st.button("Submit"):
    trimmed_prompt = prompt.strip()
    if not trimmed_prompt:
        st.error("Please enter a prompt before submitting.")
    elif len(trimmed_prompt) > MAX_INPUT_CHARS:
        st.error(f"Please enter a prompt no more than {MAX_INPUT_CHARS} characters.")
    elif st.session_state.request_count >= MAX_REQUESTS_PER_SESSION:
        st.error(f"You have reached the maximum number of requests ({MAX_REQUESTS_PER_SESSION}).")
    else:
        try:
            with st.spinner("Generating response…"):
                st.session_state.reply = fetch_reply(trimmed_prompt)
                st.session_state.request_count += 1
        except Exception as exc:
            st.error(str(exc))

st.text_area("Response", value=st.session_state.reply, height=240, disabled=True)
