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
ford_models = ['C-Max', 'Edge', 'Fiesta', 'Focus', 'Fusion', 'Galaxy', 'Grand C-Max', 'KA Plus','KA',
              'Kuga', 'Mondeo', 'Puma', 'Mustang', 'Ranger', 'S-Max', 'Transit Custom', 'Transit', 'B-Max']

car_input['make'] = st.selectbox('Please select the car make:', car_makes)

if 'Audi' in car_input['make']:
    car_input['model'] = st.selectbox('Please select the car model:', audi_models)
    
if 'Ford' in car_input['make']:
    car_input['model'] = st.selectbox('Please select the car model:', ford_models)
    