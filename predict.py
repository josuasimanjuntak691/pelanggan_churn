import joblib
import pandas as pd
import numpy as np
import streamlit as st 

model = joblib.load('model_churn_xgb.pkl')

def run():
  st.title('Prediksi Customer Churn')

  with st.form('churn telco'):
    senior = st.selectbox('Senior citizen', ('No', 'Yes'))
    partner = st.selectbox('Partner', ('No', 'Yes'))
    dependents = st.selectbox('Dependents', ('No', 'Yes'))
    tenure = st.slider('Tenure (bulan)', min_value=0, max_value=72, value=12)
    monthly = st.number_input('Monthly charges', min_value=18.0, max_value=120.0, value=70.0)
    contract = st.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
    paperless = st.selectbox('Paperless billing', ('Yes', 'No'))
    payment = st.selectbox('Payment method', ('Electronic check', 'Mailed check',
                                              'Bank transfer (automatic)', 'Credit card (automatic)'))
    multiple_lines = st.selectbox('Multiple lines', ('No', 'Yes', 'No phone service'))
    internet = st.selectbox('Internet service', ('DSL', 'Fiber optic', 'No'))
    online_security = st.selectbox('Online security', ('No', 'Yes'))
    online_backup = st.selectbox('Online backup', ('No', 'Yes'))
    device_protection = st.selectbox('Device protection', ('No', 'Yes'))
    tech_support = st.selectbox('Tech support', ('No', 'Yes'))
    streaming_tv = st.selectbox('Streaming TV', ('No', 'Yes'))
    streaming_movies = st.selectbox('Streaming movies', ('No', 'Yes'))

    submitted = st.form_submit_button('Predict')

  # jika tidak punya internet, layanan tambahan otomatis "No internet service"
  if internet == 'No':
    online_security = 'No internet service'
    online_backup = 'No internet service'
    device_protection = 'No internet service'
    tech_support = 'No internet service'
    streaming_tv = 'No internet service'
    streaming_movies = 'No internet service'

  data_inf = {
    'SeniorCitizen': 1 if senior == 'Yes' else 0,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'MultipleLines': multiple_lines,
    'InternetService': internet,
    'OnlineSecurity': online_security,
    'OnlineBackup': online_backup,
    'DeviceProtection': device_protection,
    'TechSupport': tech_support,
    'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies,
    'Contract': contract,
    'PaperlessBilling': paperless,
    'PaymentMethod': payment,
    'MonthlyCharges': monthly,
    'TotalCharges': tenure * monthly
  }

  data_inf = pd.DataFrame([data_inf])
  data_inf['SeniorCitizen'] = data_inf['SeniorCitizen'].astype('object')

  if submitted:
    pred = model.predict(data_inf)[0]

    if pred == 1:
      st.error('Pelanggan diprediksi CHURN')
    else:
      st.success('Pelanggan diprediksi TIDAK CHURN')

if __name__ == '__main__':
  run()