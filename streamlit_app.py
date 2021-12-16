import pandas as pd
import streamlit as st
import numpy as np

st.title('We buy almost any car.com')

car_input = {'make':'xyz',
'model':'xyz',
'year':'xyz',
'mileage':'xyz',
'BHP':'xyz',
'transmission':'xyz',
'fuel':'xyz',
'owners':'xyz',
'body':'xyz',
'ULEZ':'xyz',
'Engine':'xyz',
}

car_makes = ['Audi', 'Ford', 'Mercedes', 'Nissan', 'Vauxhall', 'Volkswagen', '']

audi_models = ['A1', 'A3', 'A4', 'A5', 'A6', 'Q2', 'Q3', 'Q5', 'Q7', 'S3', 'TT']
ford_models = ['B-Max', 'C-Max', 'Edge', 'Fiesta', 'Focus', 'Fusion', 'Galaxy', 'Grand C-Max', 'KA', 'KA Plus',
              'Kuga', 'Mondeo', 'Mustang', 'Puma', 'Ranger', 'S-Max', 'Transit', 'Transit Custom']
mercedes_models = ['A_Class', 'B_Class', 'C_Class', 'CLA_Class', 'E_Class', 'GLA_Class', 'GLC_Class', 'GLE_Class',
                   'S_Class']
nissan_models = []
vauxhall_models = []
volkswagen_models = []
_models = []

car_input['make'] = st.selectbox('Please select the car make:', car_makes)

if 'Audi' in car_input['make']:
    car_input['model'] = st.selectbox('Please select the car model:', audi_models)
    
elif 'Ford' in car_input['make']:
    car_input['model'] = st.selectbox('Please select the car model:', ford_models)

elif 'Mercedes' in car_input['make']:
    car_input['model'] = st.selectbox('Please select the car model:', mercedes_models)
    
elif 'Nissan' in car_input['make']:
    car_input['model'] = st.selectbox('Please select the car model:', nissan_models)
    
elif 'Vauxhall' in car_input['make']:
    car_input['model'] = st.selectbox('Please select the car model:', vauxhall_models)
    
elif 'Volkswagen' in car_input['make']:
    car_input['model'] = st.selectbox('Please select the car model:', volkswagen_models)
    
else :
    car_input['model'] = st.selectbox('Please select the car model:', _models)
    
ulez = ['Yes', 'No']
car_input['ULEZ'] = st.radio('Is the car ULEZ compliant:', ulez)

car_input['mileage'] = st.slider('Car mileage' , min_value=0, max_value=15000, value=500, step=10)