import streamlit as st
from geopy.geocoders import Nominatim
import datetime as dt
import meteomatics.api as api
from runnow_helper import run_now_raw 
from secret_key import meteomatics_username,meteomatics_password

username = meteomatics_username
password = meteomatics_password


def main():
    st.title("Can I Run NOW?")

    # Get user input
    input_string = st.text_input("Enter your location")
    
    depth = st.slider("Depth in hours", min_value=3, max_value=18, value=10)

    # Process the input (you can customize this based on your requirements)
    waterlogging = run_now_raw(input_string,depth)
    # Display the output
    if st.button("Predict"): 
      st.write("Waterlogging severity is", waterlogging)


    st.text("Usage Instructions")

    

if __name__ == "__main__":
    main()
