import streamlit as st

st.set_page_config(page_title="Marks Calculator", layout="centered")

st.title("📊 Marks Calculator - Final Score Out of 50")

st.header("Enter Marks")
num_subjects = st.number_input("Number of Internal Assessments", min_value=1, max_value=5, value=2)

marks = []
for i in range(num_subjects):
    mark = st.number_input(f"IA {i + 1} Marks", min_value=0.0, max_value=25.00, value=0.0)
    marks.append(mark)

if marks:
    average = sum(marks) / len(marks)
    st.write(f"🔹 **Average Marks:** {average:.2f}")

    st.header("Scaling ")
    scale_to = st.number_input("Enter scale value ")
    ia_score=(average*scale_to)/25
    st.write(f"📈 **Scaled Average:** {ia_score}")

    st.header("Assignment and Quiz")
    assignment = st.number_input("Assignment Marks (out of 10)", min_value=0.0, max_value=25.0, value=0.0)
    quiz = st.number_input("Quiz Marks or Lab (out of 10)", min_value=0.0, max_value=10.0, value=0.0)
    scale_assig=(assignment*25)/10
    st.header("Final Calculation")
    final_score = min(ia_score+ scale_assig + quiz, 50.0)
    st.success(f"🏁 Final Score: **{final_score:.2f} / 50**")
    
    st.write("***by Mounesh.C.Badiger***")
