import streamlit as st
import pandas as pd

# Page Title
st.title("Financial Resolution Planner")

# Subheader for Budgeting
st.subheader("Budgeting Tools")

# Create a DataFrame to store expense data
expense_data = pd.DataFrame(columns=['Category', 'Amount'])

# Collect user input for expenses
st.subheader("Expense Tracking")
expense_category = st.text_input("Enter expense category:")
expense_amount = st.number_input("Enter expense amount:", value=0.0)

# Button to add expense
if st.button("Add Expense"):
    expense_data = pd.concat([expense_data, pd.DataFrame({'Category': [expense_category], 'Amount': [expense_amount]})], ignore_index=True)
    st.success(f"Expense added successfully!\n\nCategory: {expense_category}\nAmount: ${expense_amount:.2f}")

# Display the entered expenses
st.subheader("Expense Summary")
st.table(expense_data)

# Analyze expenses
if not expense_data.empty:
    st.subheader("Expense Analysis")
    category_expenses = expense_data.groupby('Category')['Amount'].sum()
    st.bar_chart(category_expenses)
