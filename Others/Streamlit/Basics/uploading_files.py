import streamlit as st
import pandas as pd



st.title('Upload Files')
st.subheader('Image')
uploaded_file = st.file_uploader(label='Upload an Image',type='jpg')

if uploaded_file is not None:
    st.write(uploaded_file.size) 
    st.image(image=uploaded_file)


st.subheader('Video')
uploaded_file = st.file_uploader(label='Upload an Image',type='mp4')

if uploaded_file is not None:
    st.write(uploaded_file.size) 
    st.video(data=uploaded_file)






