import streamlit as st
from Home import Home
from dashboard import dashboard_page
from chatbot import chatbot_page
from cityandgases import city_and_gases
def main():
    
        st.sidebar.title("Menu")
        sidebar = st.sidebar.radio("",["🛖 Home", "🌍 About Gases and cities", "📊 Dashboard", "🤖 Chatbot"])

        if sidebar == "🛖 Home":
            Home()
        elif sidebar == "🌍 About Gases and cities":
            city_and_gases()
        elif sidebar == "📊 Dashboard":
            dashboard_page()
        elif sidebar == "🤖 Chatbot":
            chatbot_page()
           
if __name__ == "__main__":
    main()
