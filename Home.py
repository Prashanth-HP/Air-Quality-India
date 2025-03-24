import streamlit as st

def Home():
    st.title("🌍 Welcome to Your Air Quality Companion!")
    
    # Add a welcoming image (Ensure you have 'home_banner.jpg' in your project)

    st.markdown(
        """
        ### Hey there! 👋  
        Ever wondered how clean the air around you really is? You're in the right place!  
        Our **Air Quality Monitoring App** helps you track pollution levels, compare cities, and make informed choices for a healthier life. 🌱💨
        """
    )

    st.divider()

    st.subheader("🚀 What You Can Do Here")
    st.write("Here's what makes this app awesome:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("📍 **City-wise Pollution Analysis** – Compare different locations")
        st.markdown("📊 **Interactive Dashboards** – Visualize trends easily")
        st.markdown("🌍 **Make Healthier Choices** – Breathe better, live better")

    with col2:
        st.markdown("💡 **Understand Gases & Pollutants** – Learn what affects your health")
        st.markdown("🤖 **Data-Driven Chatbot.** – Ask questions, get insights")


    st.divider()

    st.subheader("🛠️ How to Get Started?")
    st.markdown(
        """
        - 📊 **Go to the Dashboard** → Explore real-time pollution data  
        - 📍 **Check Info Section** → Understand pollutants & gases  
        - 💬 **Chat with our bot** → Get quick air quality insights  
        """
    )

    st.warning("Your health matters. Stay informed. Breathe fresh! 😊")

