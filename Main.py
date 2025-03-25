import streamlit as st
from Home import Home
from dashboard import dashboard_page
from chatbot import chatbot_page
from cityandgases import city_and_gases
custom_css = """
<style>
    /* Apply gradient background */
    .stApp {
        background: linear-gradient(135deg, #FF4B4B, #1E1E1E);
        color: white;
    }

    /* Customize text */
    h1, h2, h3, h4, h5, h6, p, div {
        color: white !important;
    }

    /* Style the sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #1E1E1E, #FF4B4B);
        color: white;
    }

    /* Custom button style */
    .stButton > button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }

    .stButton > button:hover {
        background-color: #E94444;
    }
</style>
"""

# Inject CSS into Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

def main():
    
        st.sidebar.title("Menu")
        sidebar = st.sidebar.radio("",["Home", "About Gases ans cities", "Dashboard", "Chatbot"])

        if sidebar == "Dashboard":
            dashboard_page()
        elif sidebar == "Home":
            Home()
        elif sidebar == "About Gases ans cities":
            city_and_gases()
        elif sidebar == "Chatbot":
            chatbot_page()
        
        
if __name__ == "__main__":
    main()
