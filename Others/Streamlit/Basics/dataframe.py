import streamlit as st
import pandas as pd

import pandas as pd

data = []

# Create 10 rows and 10 columns
for row in range(10):
    row_data = []
    for column in range(10):
        value = f'Value at Row {row+1}, Column {column+1}'
        row_data.append(value)
    data.append(row_data)

# Create DataFrame
df = pd.DataFrame(data, columns=[f'Column {column+1}' for column in range(10)],
                  index=[f'Row {row+1}' for row in range(10)])

# Print the DataFrame

st.title('working with dataframe')

st.subheader('this is table function')
st.table(df)

st.subheader('this is dataframe function')
st.dataframe(df)
