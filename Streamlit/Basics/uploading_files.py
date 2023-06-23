import streamlit as st
import pandas as pd



st.title('Upload Files')

uploaded_file = st.file_uploader(label='Upload an Image')
st.write(uploaded_file) 

