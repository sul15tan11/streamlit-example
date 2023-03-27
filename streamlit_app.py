from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai
import gradio

openai.api_key = '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'

"""
# أهلا بك في المساعد الشخصي لطلاب جامعة الحدود الشمالية!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""




st.title("🤖 chatBot : openAI GPT-3 + Streamlit")


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 


user_input = get_text()

