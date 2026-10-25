"""DVN36104 Session 2E — official-style multipage tutorial app."""
import streamlit as st

st.set_page_config(page_title='Streamlit Multipage Tutorial',page_icon='🧭')
st.title('🧭 Streamlit multipage app')
st.markdown('This app demonstrates Streamlit’s `pages/` folder navigation. '
            'Choose a demo in the sidebar to explore charts, maps and tables.')
st.info('Three separate Python page files are detected automatically by Streamlit.')
st.markdown('**Built for DVN36104 — Asynchronous Session 2, Part E.**')
