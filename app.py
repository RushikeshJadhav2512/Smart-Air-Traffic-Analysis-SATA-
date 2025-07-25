import streamlit as st
import pandas as pd
from src.controller.flight_delay_controller import FlightDelayController


def main():
    st.set_page_config(page_title="SMART AIR TRAFFIC ANALYSIS WITH MACHINE LEARNING", layout="wide")
    
    # Initialize the controller
    controller = FlightDelayController()

    # Create the Streamlit app
    st.sidebar.title("SMART AIR TRAFFIC ANALYSIS WITH MACHINE LEARNING & Model Monitoring App")
    choice = st.sidebar.radio("Select an option:", ("Make Predictions", "Monitor Data and Model"))

    if choice == "Make Predictions":
        controller.run_prediction()

    elif choice == "Monitor Data and Model":
        controller.run_monitoring()
        

if __name__ == '__main__':
    main()
