from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import openai

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


openai.api_key = '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'

messages = [{"role": "system", "content": "You are a programming assistant for Northern Border University students. - Follow the user's requirements carefully & to the letter. - First think step-by-step - describe your plan for what to build in pseudocode in Arabic language, written out in great detail. - Then output the code in a single code block. - Minimize any other prose"}]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    
