import streamlit as st

def city_and_gases():
    st.title("Explanation of Gases in the Dataset")
    st.write("The dataset includes 8 air pollutants that are harmful to human health and the environment:")

    st.header("NH3 (Ammonia)")
    st.markdown(
        """
        - **Source**: Agriculture (fertilizers, livestock waste), industrial processes.
        - **Effects**: Causes respiratory irritation and contributes to the formation of fine particulate matter (PM2.5).
        """
    )

    st.header("CO (Carbon Monoxide)")
    st.markdown(
        """
        - **Source**: Vehicle emissions, burning of fossil fuels, wildfires.
        - **Effects**: Reduces oxygen delivery in the body, leading to headaches, dizziness, or even death at high concentrations.
        """
    )

    st.header("PM2.5 (Fine Particulate Matter)")
    st.markdown(
        """
        - **Source**: Vehicle emissions, industrial activities, burning of biomass and coal.
        - **Effects**: Can penetrate deep into the lungs, causing respiratory diseases, heart problems, and cancer.
        """
    )

    st.header("PM10 (Coarse Particulate Matter)")
    st.markdown(
        """
        - **Source**: Construction dust, road dust, industrial emissions.
        - **Effects**: Causes lung irritation, worsens asthma, and affects cardiovascular health.
        """
    )

    st.header("NO (Nitric Oxide)")
    st.markdown(
        """
        - **Source**: Vehicle emissions, power plants, and industrial combustion.
        - **Effects**: Contributes to smog formation, reduces lung function, and reacts with other pollutants to form NO₂.
        """
    )

    st.header("NO2 (Nitrogen Dioxide)")
    st.markdown(
        """
        - **Source**: Fossil fuel combustion, vehicle emissions, industrial processes.
        - **Effects**: Causes lung inflammation, worsens asthma, and contributes to acid rain formation.
        """
    )

    st.header("NOx (Nitrogen Oxides - NO + NO2 mixture)")
    st.markdown(
        """
        - **Source**: Combustion of fuel in vehicles, power plants, and industrial facilities.
        - **Effects**: Major contributor to smog, acid rain, and respiratory illnesses.
        """
    )

    st.header("SO2 (Sulfur Dioxide)")
    st.markdown(
        """
        - **Source**: Coal and oil burning in power plants, industrial facilities.
        - **Effects**: Causes respiratory issues, contributes to acid rain, and can damage crops.
        """
    )

    st.title("Cities Covered in the Dataset")
    st.write(
        "This dataset includes air quality data from **26 Indian cities**, including major metro cities such as Delhi, Mumbai, Kolkata, Chennai, Bengaluru, Hyderabad, etc., along with smaller cities like Shillong, Talcher, Jorapokhar, Brajrajnagar, etc."
    )

    st.header("Why These Cities?")
    st.markdown(
        """
        - These cities likely have high pollution levels due to urbanization, industrialization, and vehicular emissions.
        - Metro cities (like Delhi and Mumbai) experience high PM2.5 and NO2 levels due to traffic and industries.
        - Industrial towns (like Talcher and Brajrajnagar) may have high SO2 and NOx levels due to power plants and factories.
        - Smaller cities (like Shillong and Aizawl) might show lower pollution levels due to fewer industries.
        """
    )

    st.title("How Can You Use This Data?")
    st.markdown(
        """
        - **Monitor Air Quality Trends** – Analyze how pollution levels change over time in different cities.
        - **Compare Pollution Levels** – Identify the most and least polluted cities for specific pollutants.
        - **Policy & Awareness** – Help policymakers implement air quality improvement measures.
        - **Predict Future Trends** – Use Machine Learning to forecast pollution spikes and take preventive actions.
        """
    )

# To run the function in a Streamlit app, call city_and_gases() inside Streamlit's main logic.
if __name__ == "__main__":
    city_and_gases()
