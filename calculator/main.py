import streamlit as st

st.title("Calculator")

num1 = int(st.number_input("Enter first number"))
num2 = int(st.number_input("Enter second number"))

operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

result = None



if operation == "Add":
    result = num1 + num2

if operation == "Subtract":
    result = num1 - num2

if operation == "Multiply":
    result = num1 * num2

if operation == "Divide":
    result = num1 / num2

if result is not None:
    st.write("Result: ", result)
