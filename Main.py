import streamlit as st
from Home import Home
from dashboard import dashboard_page
from chatbot import chatbot_page
from cityandgases import city_and_gases

def set_theme():
    """Apply selected theme dynamically."""
    theme = st.session_state.get("theme", "light")

    # Define themes
    themes = {
        "light": {
            "primaryColor": "#1E88E5",
            "backgroundColor": "#F0F2F6",
            "secondaryBackgroundColor": "#E3E4E8",
            "textColor": "#000000",
            "font": "sans serif"
        },
        "dark": {
            "primaryColor": "#BB86FC",
            "backgroundColor": "#121212",
            "secondaryBackgroundColor": "#1F1F1F",
            "textColor": "#E0E0E0",
            "font": "monospace"
        }
    }

    selected_theme = themes.get(theme, themes["light"])

    # Apply theme dynamically
    st.markdown(
        f"""
        <style>
        :root {{
            --primary-color: {selected_theme["primaryColor"]};
            --background-color: {selected_theme["backgroundColor"]};
            --secondary-background-color: {selected_theme["secondaryBackgroundColor"]};
            --text-color: {selected_theme["textColor"]};
        }}
        body {{
            background-color: var(--background-color);
            color: var(--text-color);
        }}
        .stButton>button {{
            background-color: var(--primary-color);
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


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
