import streamlit as st

def dashboard_page():
    st.title("Power BI Dashboard")

    # Create two columns to display images side by side
    col1, col2 = st.columns(2)

    with col1:
        st.image("page1.png", caption="Air Quality Index Dashboard", use_container_width=True)

    with col2:
        st.image("page2.png", caption="Pollutant Levels by City", use_container_width=True)

    st.write("Due to a technical issue on our side, we are unable to display the report online, [Install PowerBI Desktop](https://apps.microsoft.com/detail/9ntxr16hnw1t?launch=true&mode=full&hl=en-us&gl=in&ocid=bingwebsearch) , download below given pbix file and view the report ")
    #st.write("[Install PowerBI Desktop](https://apps.microsoft.com/detail/9ntxr16hnw1t?launch=true&mode=full&hl=en-us&gl=in&ocid=bingwebsearch)")
    # Provide download option for the Power BI file
    pbix_file_path = "Final Dashboard.pbix"  # Ensure the file is in the correct location
    
    with open(pbix_file_path, "rb") as file:
        st.download_button(
            label="Download Power BI Dashboard (.pbix)",
            data=file,
            file_name="Final Dashboard.pbix",
            mime="application/octet-stream"
        )
