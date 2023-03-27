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
   

import streamlit as st
import streamlit.components.v1 as components
import requests

def theTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res = response.json()["html"]
    return res

input = st.text_input("Enter your tweet url")
if input:
    res = theTweet(input)
    st.write(res)
    components.html(res,height= 700)
