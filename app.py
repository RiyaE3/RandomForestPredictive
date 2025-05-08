import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

# Load the model
with open('randomForest.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Predict Temperature Sensor 1')

# Number inputs with step=0.0001 for 4 decimal places
soc = st.number_input('SOC', value=72.0000, step=0.0001, format="%.4f")
voltage = st.number_input('Voltage', value=51.4000, step=0.0001, format="%.4f")
current = st.number_input('Current', value=29.1000, step=0.0001, format="%.4f")

# Default cell voltages
default_cell_voltages = [3.269, 3.266, 3.267, 3.266, 3.25, 3.246, 3.252, 3.243, 
                        3.232, 3.25, 3.25, 3.25, 3.25, 3.247, 3.247, 3.263]

cell_voltages = []
for i in range(1, 17):
    cell_volt = st.number_input(f'Cell Volt {i}', value=default_cell_voltages[i-1], step=0.0001, format="%.4f")
    cell_voltages.append(cell_volt)

temp_sensor_2 = st.number_input('Temperature Sensor 2', value=33.0000, step=0.0001, format="%.4f")
temp_sensor_3 = st.number_input('Temperature Sensor 3', value=33.0000, step=0.0001, format="%.4f")
temp_sensor_4 = st.number_input('Temperature Sensor 4', value=33.0000, step=0.0001, format="%.4f")
temp_sensor_5 = st.number_input('Temperature Sensor 5', value=33.0000, step=0.0001, format="%.4f")

if st.button('Predict Temperature Sensor 1'):
    input_data = np.array(
        [[soc, voltage, current] + cell_voltages + [temp_sensor_2, temp_sensor_3, temp_sensor_4, temp_sensor_5]])

    prediction = model.predict(input_data)

    st.success(f'Predicted Temperature Sensor 1: {prediction[0]:.2f} °C')

