# the first machine learning app with streamlit
# uses google translator
# june 2020
# usage: streamlit run app.py
# dependencies: 
#pip install streamlit # the awesome framework
#pip install vaderSentiment # for sentimental analysis
#pip install googletrans # for language translation
# ref: https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2

import streamlit as st
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer() # initialize it
translator = Translator() # initialize

st.markdown("# Machine Learning App Registry")
st.markdown("## App 1: Multilingual Sentimental Analysis")
st.write("Sentimental Analysis is a branch of Natural Language Processing")

def sentiment_analyzer_scores(sentence):
   trans = translator.translate(sentence).text # extracting   translation text
   score = analyser.polarity_scores(trans) # analyzing the text
   score = score["compound"]
   if score >= 0.05:
      return "The sentiment of your text is Positive"
   elif score > -0.5 and score < 0.05:
      return "The sentiment of your text is Neutral"
   else:
      return "The sentiment of your text is Negative"
   return score

sentence = st.text_area("Write your sentence") # we take user input
if st.button("Submit"): # a button for submitting the form
   result = sentiment_analyzer_scores(sentence) # run our function  on it
   st.balloons() # show some cool animation
   st.success(result) # show result in a Bootstrap panel

