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
'ulez':'xyz',
'engine':'xyz',
}

car_makes = ['Audi', 'Ford', 'Mercedes', 'Nissan', 'Vauxhall', 'Volkswagen', '']
car_input['make'] = st.selectbox('Please select the car make:', car_makes)

audi_models = ['A1', 'A3', 'A4', 'A5', 'A6', 'Q2', 'Q3', 'Q5', 'Q7', 'S3', 'TT']
ford_models = ['B-Max', 'C-Max', 'Edge', 'Fiesta', 'Focus', 'Fusion', 'Galaxy', 'Grand C-Max', 'KA', 'KA Plus',
              'Kuga', 'Mondeo', 'Mustang', 'Puma', 'Ranger', 'S-Max', 'Transit', 'Transit Custom']
mercedes_models = ['A Class', 'B Class', 'C Class', 'CLA Class', 'E Class', 'GLA Class', 'GLC Class', 'GLE Class',
                   'S Class']
nissan_models = ['370Z', 'Elgrand', 'Juke', 'Micra', 'Navara', 'Pixo', 'Qashqai', 'X-trail']
vauxhall_models = ['Adam', 'Astra', 'Corsa', 'Crossland X', 'Grandland X', 'Insignia', 'Mokka', 'Non-Franchise C']
volkswagen_models = ['Beetle', 'Golf', 'Passat', 'Polo', 'Scirocco', 'T-Roc', 'Tiguan', 'Up']
_models = []

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
    

    
audi_bodys = ['Convertible', 'Coupe', 'Estate', 'Hatchback','Saloon', 'SUV']
ford_bodys = ['Convertible', 'Coupe', 'Estate', 'Hatchback', 'MPV', 'Pickup', 'Saloon', 'SUV']
mercedes_bodys = ['Convertible', 'Coupe', 'Estate', 'Hatchback', 'MPV', 'Saloon', 'SUV']
nissan_bodys = ['Convertible', 'Coupe', 'Estate', 'Hatchback', 'MPV', 'Pickup', 'SUV']
vauxhall_bodys = ['Convertible', 'Estate', 'Hatchback','Saloon', 'SUV']
volkswagen_bodys = ['Convertible', 'Coupe', 'Estate', 'Hatchback', 'Saloon', 'SUV']
_bodys = []

if 'Audi' in car_input['make']:
    car_input['body'] = st.selectbox('Please select the car model:', audi_bodys)
    
elif 'Ford' in car_input['make']:
    car_input['body'] = st.selectbox('Please select the car model:', ford_bodys)

elif 'Mercedes' in car_input['make']:
    car_input['body'] = st.selectbox('Please select the car model:', mercedes_bodys)
    
elif 'Nissan' in car_input['make']:
    car_input['body'] = st.selectbox('Please select the car model:', nissan_bodys)
    
elif 'Vauxhall' in car_input['make']:
    car_input['body'] = st.selectbox('Please select the car model:', vauxhall_bodys)
    
elif 'Volkswagen' in car_input['make']:
    car_input['body'] = st.selectbox('Please select the car model:', volkswagen_bodys)
    
else :
    car_input['body'] = st.selectbox('Please select the car model:', _bodys)


    
car_year = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010',
            '2009', '2008', '2007', '2006', '2005', 'Before 2005']
car_input['year'] = st.selectbox('Please select the car year:', car_year)
    
car_input['mileage'] = st.text_input('Please enter the car mileage:')

car_transmission = ['Automatic', 'Manual']
car_input['transmission'] = st.radio('What transmission does the car have?', car_transmission)

car_fuel = ['Petrol', 'Diesel']
car_input['fuel'] = st.radio('What fuel does the car use?', car_fuel)

car_input['engine'] = st.slider('What is the car engine size? (l)', min_value=0.0, max_value=9.0, step=0.1)

car_input['owners'] = st.slider('How many owners has the car had?', min_value=0, max_value=100, step=1)
    
ulez = ['Yes', 'No']
car_input['ulez'] = st.radio('Is the car ULEZ compliant?', ulez)

st.button("Price", key=None, help=None, on_click=None, args=None, kwargs=None)
