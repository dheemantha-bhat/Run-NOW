import streamlit as st
from geopy.geocoders import Nominatim
import datetime as dt
import meteomatics.api as api
from runnow_helper import run_now_raw 



def main():
  
    st.title("Can I Run NOW?")
    st.subheader('Usage Instructions')
    st.text('Run-NOW predicts waterlogging severity based on observed rainfall.')
    st.text('Step 1 : Enter your Meteomatics API credentials')
    st.text('Step 2 : Enter the location in search bar ')
    st.text('Step 3 : Choose the depth of prediction i.e. Number of hours of observed rainfall \n used for prediction')
    
    api_key = st.text_input("Enter API Key:")
    secret_key = st.text_input("Enter Secret Key:", type="password")
    st.button('Submit')

    input_string = st.text_input("Enter your location")
    
    depth = st.slider("Depth in hours", min_value=3, max_value=18, value=10)

    waterlogging = run_now_raw(input_string,depth,api_key, secret_key)

    if st.button("Predict"): 
      st.write("Waterlogging severity")
      
      if waterlogging=='High':
        st.markdown(''':red[High]''')
      if waterlogging=='Medium':
        st.markdown(''':orange[Medium]''')
      else:
        st.markdown(''':green[Low]''' )

 
if __name__ == "__main__":
    main()
