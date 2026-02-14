# Assignment:(hands on)
import streamlit as st
import pandas as pd

# Profile

st.title("Take It Smart")
st.header("Role: Data Scientist")
st.write("Skills: Python, Machine Learning, MySQL, FSD")

st.divider()


# User input

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0)

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)

st.divider()


# Checkbox

if st.checkbox("Show text"):
    st.write("Hello! This text is visible.")

st.divider()

# Selectbox

language = st.selectbox(
    "Choose a programming language",
    ["Python", "Java", "JavaScript", "C++"]
)
st.write("Selected language:", language)

st.divider()


# Counter (no session state)

count = 0
if st.button("Increase Counter"):
    count += 1
st.write("Counter value:", count)

st.divider()


# DataFrame display

data = {
    "Name": ["Asha", "Ravi", "Neha"],
    "Age": [22, 25, 23]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.divider()


# CSV upload

uploaded_file = st.file_uploader("Upload CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.divider()

# Sidebar

course = st.sidebar.selectbox(
    "Select Course",
    ["Data Science", "Full Stack Python", "Full Stack Java", "Oracle"]
)
st.sidebar.write("Selected:", course)


# Success message

if st.button("Show Success"):
    st.success("Button clicked successfully!")
