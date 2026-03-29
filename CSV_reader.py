import pandas as pd
import streamlit as st
df = pd.read_csv("Student.csv")
st.title("Student CSV Reader")
st.subheader("All Student Data")
st.dataframe(df)
st.subheader("Search for a Student")
student_name = st.text_input("Enter the students's name: ")
if student_name:
    result = df[df["Name"].str.strip().str.lower() == student_name.strip().lower()]
    if not result.empty:
        st.write("Here is the data for", student_name)
        st.dataframe(result)
    else:
        st.warning("No student found with that name")