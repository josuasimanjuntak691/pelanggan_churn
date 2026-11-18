import streamlit as st 
import eda
import predict


st.set_page_config(
    layout='wide',
    initial_sidebar_state='expanded',
    page_title='prediksi Churn'
)

page = st.sidebar.selectbox('pilih halaman', ('eda','predict'))
if page == 'eda':
    eda.run()
else:
    predict.run()