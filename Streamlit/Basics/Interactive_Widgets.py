import streamlit as st
import pandas as pd

st.title('Interactive Widgets')

st.subheader('Checkbox')
state = st.checkbox(label='Hello',value=True)

if state==True:
    st.write('Hiiiiiiiii')
else:
    st.write('byyy')

st.subheader('radio Button')
radio_btn = st.radio(label='what is your favourite color?(radio Button)',options=['green ','blue','yello','black','read'])
st.write(radio_btn)

if radio_btn =='hello':
    st.write('radio button - Hello')  
else:
    st.write('radio button - hii')


st.subheader('Select Box')
st.selectbox(label='what is your favourite color?(select box)',options=['green ','blue','yello','black','read'])


st.subheader('Multiple Select Box')
multiselectBox = st.multiselect(label='what is your favourite color?(Multiple Select Box)',options=['green ','blue','yello','black','read'])
print(multiselectBox)
st.write(multiselectBox)
