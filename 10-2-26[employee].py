import streamlit as st
import pandas as pd

st.title("Employee Management App")

# =====================================================
# Upload CSV
# =====================================================
st.header("Upload Employee CSV")

file = st.file_uploader("Upload file", type="csv")

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Original Data")
    st.dataframe(df)

    # Filter salary > 50000
    st.subheader("Employees with Salary > 50,000")
    high_salary = df[df["Salary"] > 50000]
    st.dataframe(high_salary)

st.divider()

# =====================================================
# Role selection
# =====================================================
st.header("Select Your Role")

role = st.selectbox(
    "Choose role",
    ["Admin", "Manager", "Employee"]
)

# Show different content
if role == "Admin":
    st.success("Welcome Admin! You can manage employees.")

elif role == "Manager":
    st.success("Welcome Manager! You can view reports.")

elif role == "Employee":
    st.success("Welcome Employee! You can check your details.")
