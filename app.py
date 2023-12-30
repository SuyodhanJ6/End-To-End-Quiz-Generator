import streamlit as st
from mcqGenerator.pipeline import initialization_of_quiz

def display_generated_quiz(quiz):
    st.write("### Generated MCQ:")
    for question_number, question_data in quiz.items():
        st.write(f"**Question {question_number}:** {question_data['mcq']}")
        options = question_data['options']
        st.write(f"Options: {', '.join([f'{key}: {value}' for key, value in options.items()])}")
        st.write(f"Correct Answer: {question_data['correct']}")
        st.write("---")

def main():
    st.title("MCQ Generator Web App")

    # Button to trigger MCQ generation
    if st.button("Generate MCQ"):
        quiz = initialization_of_quiz()
        display_generated_quiz(quiz)

if __name__ == "__main__":
    main()
