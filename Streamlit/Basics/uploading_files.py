import streamlit as st
import pandas as pd



st.title('Upload Files')
st.subheader('Image')
uploaded_file = st.file_uploader(label='Upload an Image',type='jpg')
st.write(uploaded_file.size) 

st.image(image=uploaded_file)


st.subheader('Video')
uploaded_file = st.file_uploader(label='Upload an Image',type='mp4')
st.write(uploaded_file) 

st.video(data=uploaded_file)






