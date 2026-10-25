"""DVN36104 Session 2C — Streamlit's official Uber pickups tutorial."""
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title='NYC Uber Pickups',page_icon='🚕',layout='wide')
st.title('🚕 Uber pickups in New York City')
st.caption('A tutorial app: cached data, hourly histogram, map, slider, and raw-data toggle.')
DATE_COLUMN='date/time'
DATA_URL='https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

@st.cache_data(show_spinner='Loading public NYC pickup data…')
def load_data(nrows:int):
    data=pd.read_csv(DATA_URL,nrows=nrows)
    data.columns=[str(name).lower() for name in data.columns]
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data

data=load_data(10000)
st.success(f'Loaded {len(data):,} pickups (cached).')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.dataframe(data,width='stretch')

st.subheader('Number of pickups by hour')
hist_values=np.histogram(data[DATE_COLUMN].dt.hour,bins=24,range=(0,24))[0]
st.bar_chart(pd.DataFrame({'hour':np.arange(24),'pickups':hist_values}).set_index('hour'))

hour=st.slider('Choose an hour',0,23,17)
filtered=data[data[DATE_COLUMN].dt.hour==hour]
st.subheader(f'Pickup locations at {hour:02d}:00')
st.caption(f'{len(filtered):,} pickup locations in the sample')
st.map(filtered)
