import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title='DataFrame Demo',page_icon='📊')
st.title('📊 Dataframe demo')
rng=np.random.default_rng(36104)
data=pd.DataFrame(rng.standard_normal((100,4)),columns=list('ABCD'))
st.dataframe(data,width='stretch')
selected=st.selectbox('Inspect a column',data.columns)
counts,edges=np.histogram(data[selected],bins=12)
st.bar_chart(pd.DataFrame({'value_mid':(edges[:-1]+edges[1:])/2,'count':counts}).set_index('value_mid'))
