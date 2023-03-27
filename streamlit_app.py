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


article_text = st.text_area("Enter your scientific texts to summarize")

# Create Radio Buttons
output_size = st.radio( label = "What kind of output do you want?", 
                        options= [“To-The-Point”, “Concise”, “Detailed”]
                     )


# First, we'll use an if statement to determine the desired output size 
# and set the out_token variable accordingly:

if output_size == “To-The-Point”:
 out_token = 50
elif output_size == “Concise”:
 out_token = 128
else:
 out_token = 516

# Next, we'll add a check to make sure that the input text is long enough 
# to summarize, and display a warning if it is not:

if len(article_text)>100:
 # Generate the summary
 # .......
else:
 st.warning("Not enough words to summarize!")
