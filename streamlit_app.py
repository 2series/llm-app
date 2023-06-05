import os

import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI

# Load environment variables
load_dotenv()

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.title("🎈 🦜🔗 Quickstart App")


def generate_response(input_text):
    llm = OpenAI(temperature=0.9)
    st.info(llm(input_text))


with st.form(key="my_form"):
    text_input = st.text_area("Enter text:", "Once upon a time, there was a")
    submit_button = st.form_submit_button(label="Submit")
    if not OPENAI_API_KEY.startswith("sk-"):
        st.warning("Please enter your OpenAI API key in the .env file!", icon="warning")
    if submit_button and OPENAI_API_KEY.startswith("sk-"):
        generate_response(text_input)
