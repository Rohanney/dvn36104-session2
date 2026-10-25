import pandas as pd
import streamlit as st

st.set_page_config(page_title='Mapping Demo',page_icon='🌍')
st.title('🌍 Mapping demo')
data=pd.DataFrame({
    'city':['Sydney','Melbourne','Brisbane','Perth','Adelaide'],
    'lat':[-33.8688,-37.8136,-27.4698,-31.9505,-34.9285],
    'lon':[151.2093,144.9631,153.0251,115.8605,138.6007],
})
st.map(data,latitude='lat',longitude='lon')
st.dataframe(data,width='stretch',hide_index=True)
