import streamlit as st
import random
import time

# Function to generate simulated emissions data
def generate_emission_data():
    energy_emission = random.uniform(50, 200)  # Energy emission in tons of CO2
    transport_emission = random.uniform(20, 100)  # Transport emission in tons of CO2
    waste_emission = random.uniform(10, 50)  # Waste emission in tons of CO2
    total_emission = energy_emission + transport_emission + waste_emission
    return energy_emission, transport_emission, waste_emission, total_emission

# Layout of the dashboard
st.title("Carbon Emissions and Sustainability Dashboard")

# Create a placeholder to update data in real-time
placeholder = st.empty()

# Streamlit Dashboard Loop
while True:
    energy_emission, transport_emission, waste_emission, total_emission = generate_emission_data()
    
    # Clear and update the placeholder
    placeholder.empty()
    with placeholder.container():
        st.subheader("Carbon Emissions Breakdown (in Tons of CO2)")
        st.write(f"### Energy Emissions: {energy_emission:.2f} tons")
        st.write(f"### Transport Emissions: {transport_emission:.2f} tons")
        st.write(f"### Waste Emissions: {waste_emission:.2f} tons")
        st.write(f"### Total Emissions: {total_emission:.2f} tons")
        
        st.subheader("Sustainability Insights")
        if total_emission > 200:
            st.warning("High emissions detected! Consider taking immediate action to reduce emissions.")
        else:
            st.success("Your emissions are within sustainable limits. Keep it up!")
    
    # Sleep for 1 second before refreshing the data
    time.sleep(1)
