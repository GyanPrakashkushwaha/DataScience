import streamlit as st
import pandas as pd

# first few codes
st.title('First Few codes')

st.header('Hello there I am header')

st.subheader('Hello there subheader')

st.text('Hello I am text')

st.markdown('# I am markdown1')
st.markdown('## I am markdown2')
st.markdown('> ## I am markdown4')
st.markdown('> ## *I am markdown5*')


st.caption('Hello I am caption How are')


st.markdown('[Hello I am Link](https://www.markdownguide.org/cheat-sheet/)')


st.write('printing code --')

code = """class online_class:
    def __init__(self,phone_num,email_id,student_id,position):
        self.phone_num = phone_num
        self.email_id= email_id
        self.student_id = student_id
        self.positon2322 = position
        
    def return_student_details(self):
        return self.student_id ,self.phone_num, self.email_id"""

st.code(code,language='python')


