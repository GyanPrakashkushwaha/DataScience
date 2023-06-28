import streamlit as st
import pandas as pd

st.title('working with media')

st.subheader('Img')
st.image(image='Streamlit\Basics\loss.png',width=1000,caption='Loss function IMG')


st.subheader('Audio')
st.audio(data='Streamlit\Basics\censor-beep-10sec-8113.mp3')

st.subheader('Video')
st.video(data='Streamlit\Face_mask_detection.mp4')
