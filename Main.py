import streamlit as st
from Home import Home
from dashboard import dashboard_page
from chatbot import chatbot_page
from cityandgases import city_and_gases
def main():
    
        st.sidebar.title("Menu")
        sidebar = st.sidebar.radio("",["🛖 Home", "🌍 About Gases and cities", "📊 Dashboard", "🤖 Chatbot"])

        if sidebar == "🛖 Home":
            dashboard_page()
        elif sidebar == "🌍 About Gases and cities":
            Home()
        elif sidebar == "📊 Dashboard":
            city_and_gases()
        elif sidebar == "🤖 Chatbot":
            chatbot_page()
           
if __name__ == "__main__":
    main()
