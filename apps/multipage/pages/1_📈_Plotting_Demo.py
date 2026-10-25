import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Plotting Demo',page_icon='📈')
st.title('📈 Plotting demo')
points=st.slider('How many points?',20,500,150,step=10)
rng=np.random.default_rng(36104)
data=pd.DataFrame(rng.standard_normal((points,3)),columns=['A','B','C']).cumsum()
st.line_chart(data)
st.caption('Change the slider to generate a reproducible random-walk plot.')
