import streamlit as st

st.title("Student GPA Prediction System")

study = st.number_input("Enter Study Hours", min_value=0, step=1)
sleep = st.number_input("Enter Sleep Hours", min_value=0, step=1)
attendance = st.number_input("Enter Attendance %", min_value=0, max_value=100, step=1)
social = st.number_input("Enter Social Media Hours", min_value=0, step=1)

if st.button("Predict GPA"):
    gpa = 0.4*study + 0.2*sleep + 0.25*(attendance/10) + 0.15*(10-social)
    st.success(f"Predicted GPA: {round(gpa,2)}") 



