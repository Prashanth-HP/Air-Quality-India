import streamlit as st
import pandas as pd
from fuzzywuzzy import process
from fpdf import FPDF

# Home Page
def Home():
    st.title("🌍 Welcome to Your Air Quality Companion!")
    st.markdown("### Hey there! 👋")
    st.write("Our **Air Quality Monitoring App** helps you track pollution levels, compare cities, and make informed choices for a healthier life. 🌱💨")

# Dashboard Page
def dashboard_page():
    st.title("Power BI Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/page1.png", caption="Air Quality Index Dashboard", use_container_width=True)
    with col2:
        st.image("data/page2.png", caption="Pollutant Levels by City", use_container_width=True)
    st.write("[Download Power BI Dashboard](https://apps.microsoft.com/detail/9ntxr16hnw1t)")

# Chatbot Page
qa_df = pd.read_csv("data/cb_questions.csv").dropna(subset=["Question", "Answer"])
qa_df["Question"] = qa_df["Question"].str.strip()

def get_best_match(user_input):
    match = process.extractOne(user_input, qa_df["Question"].dropna())
    if match and len(match) >= 2 and match[1] > 70:
        return qa_df.loc[qa_df["Question"] == match[0], "Answer"].values[0]
    return "I couldn't find an exact match. Please try rephrasing your question."

def chatbot_page():
    st.title("Chatbot")
    user_input = st.text_input("You: ", "")
    if st.button("Send"):
        st.write(f"Chatbot: {get_best_match(user_input)}")

# City and Gases Page
def city_and_gases():
    st.title("Explanation of Gases in the Dataset")
    st.header("NH3 (Ammonia)")
    st.write("Sources: Agriculture, industrial processes.")
    st.header("CO (Carbon Monoxide)")
    st.write("Sources: Vehicle emissions, fossil fuels.")

# Main Function
def main():
    st.sidebar.title("Menu")
    sidebar = st.sidebar.radio("", ["Home", "About Gases", "Dashboard", "Chatbot"])
    if sidebar == "Dashboard":
        dashboard_page()
    elif sidebar == "Home":
        Home()
    elif sidebar == "About Gases":
        city_and_gases()
    elif sidebar == "Chatbot":
        chatbot_page()

if __name__ == "__main__":
    main()
