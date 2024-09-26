import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 

# Load the model to predict on the data 
with open(r'C:\Users\dell\Downloads\Internship_Project\WalkRun-Project1\PRCP-1013-WalkRunClass\Data\LR3.pkl', 'rb') as pickle_in:
    LR3 = pickle.load(pickle_in) 

def welcome(): 
    return 'Welcome all'

# Function to make the prediction
def prediction(date, time, wrist, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z): 
    prediction = LR3.predict([[date, time, wrist, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z]]) 
    return prediction 

# Main function for the web app
def main(): 
    st.title("Walk Run Prediction") 

    # Frontend HTML
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Walk/Run Prediction App</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True) 
    
    # User input fields
    date = st.text_input("Date", "Type Here") 
    time = st.text_input("Time", "Type Here") 
    wrist = st.text_input("Wrist", "Type Here") 
    acceleration_x = st.text_input("Acceleration X", "Type Here")
    acceleration_y = st.text_input("Acceleration Y", "Type Here") 
    acceleration_z = st.text_input("Acceleration Z", "Type Here") 
    gyro_x = st.text_input("Gyro X", "Type Here") 
    gyro_y = st.text_input("Gyro Y", "Type Here")
    gyro_z = st.text_input("Gyro Z", "Type Here")
    
    result = ("","if 1 then running if 0 then walking") 

    # Predict button
    if st.button("Predict"): 
        try:
            # Convert inputs to float
            inputs = [
                float(date), float(time), float(wrist),
                float(acceleration_x), float(acceleration_y),
                float(acceleration_z), float(gyro_x),
                float(gyro_y), float(gyro_z)
            ]
            result = prediction(*inputs) 
            st.success(f'The output is: {result}')
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

if __name__ == '__main__': 
    main() 
