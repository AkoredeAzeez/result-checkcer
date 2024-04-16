import streamlit as st
import pandas as pd

# Load the data from the Excel file
excel_file = "C://Users//AKOS//Downloads//result.xlsx"  # Update with the path to your Excel file
df = pd.read_excel(excel_file)
# Load the data from the Excel file, specifying data types
df = pd.read_excel(excel_file, dtype={'MATRIC': str})

# Strip out spaces from the matric number column
df['MATRIC'] = df['MATRIC'].str.strip()

# Set page title
st.title("Student Result Checker")
page_icon=":mortar_board:",
layout="wide",  # Set layout to wide
initial_sidebar_state="expanded",  # Set sidebar state to expanded
background_color="#f0f2f6",  # Set background color
# Sidebar with input field
matric_number = st.text_input("Enter Matric Number")

# Button to display results
if st.button("Check Result"):
    result = df[df['MATRIC'] == matric_number]
    if not result.empty:
        st.write("### Result Found:")
        st.write("Full Name:", result['FULL NAME'].values[0])
        st.write("Matric No:", result['MATRIC'].values[0])
        st.write("CA:", result['CA/40'].values[0])
        st.write("Exam Score:", result['Total Exam/60'].values[0])
        st.write("Total Score:", result['Total/100'].values[0])
    else:
        st.error("Result not found for the given Matric Number.")
