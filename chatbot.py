import streamlit as st
import pandas as pd
from fuzzywuzzy import process
from fpdf import FPDF

# Load chatbot question-answer dataset
qa_file_path = "data/cb_questions.csv"
qa_df = pd.read_csv(qa_file_path)
qa_df.dropna(subset=["Question", "Answer"], inplace=True)  # Remove empty values
qa_df["Question"] = qa_df["Question"].str.strip()

def get_best_match(user_input, qa_df):
    match = process.extractOne(user_input, qa_df["Question"].dropna())
    if match and len(match) >= 2:
        best_match, score = match[0], match[1]
        if score > 70:
            return qa_df.loc[qa_df["Question"] == best_match, "Answer"].values[0]
    return "I couldn't find an exact match. Please try rephrasing your question."

def chatbot_page():
    st.title("🤖 Chatbot")
    st.write("Ask questions related to air quality!")

    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    user_input = st.text_input("You: ", "")
    
    if st.button("Send"):
        if user_input:
            st.session_state.conversation_history.append(f"You: {user_input}")
            response_text = get_best_match(user_input, qa_df)
            st.session_state.conversation_history.append(f"Chatbot: {response_text}")

    for message in st.session_state.conversation_history:
        st.write(message)

    conversation_text = "\n".join(st.session_state.conversation_history)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, conversation_text)
    pdf_output = pdf.output(dest="S").encode("latin1")

    st.download_button(
        label="Download Conversation History as PDF",
        data=pdf_output,
        file_name="conversation_history.pdf",
        mime="application/pdf"
    )
