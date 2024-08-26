import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

import pandas as pd
import datetime

with st.form("my_form"):
    st.write("Inside the form")
    d = st.date_input('Date', datetime.date())
    t = st.time_input('Time', datetime.time())
    dt = d + t

    pickup_lat = st.number_input('Pickup latitude: ')
    pickup_lon = st.number_input('Pickup longtitude: ',)
    location = pd.DataFrame(pickup_lat, pickup_lon, columns=['lat', 'lon'])

    dropoff_lon = st.number_input('Dropoff longtitude: ',)
    dropoff_lat = st.number_input('Dropoff latitude: ')
    location.loc[len(location.index)] = [dropoff_lat, dropoff_lon]

    passenger = st.number_input('Passengers: ')

    st.form_submit_button('Submit my picks')

st.map(location)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare-375233354256.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
import requests

#params
params = {

}

response = requests.get(url, params=params)
data = response.json()
pred = data['fare']

st.write(f'The predicted taxi fare is ${pred}.')
