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



# More functions

st.title('More functions')

st.subheader('Slider.')
slider =st.slider('I am a slider')
print(slider)
st.write(slider)

st.subheader('Slider with more functions')
slider =st.slider('I am a slider',min_value=50,max_value=500,value=200)
print(slider)
st.write(slider)


# st.title(' INput')
# st.subheader('camera')
# camera = st.camera_input(label='camera')
# if camera:
#     st.image(camera)
#     print(camera)

st.subheader('text')
txt = st.text_input('input',autocomplete='hello')
if txt:
    st.write(txt)


st.subheader('text area')
txt = st.text_area('input')
if txt:
    st.write(txt)

st.subheader('Date input')
txt = st.date_input('input')
if txt:
    st.write(txt)

