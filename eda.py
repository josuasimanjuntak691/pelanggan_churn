import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run():
    #membuat judul
    st.title('aplikasi prediksi pembatalan layanan')
    # membuat sub header
    st.subheader('file ini berisi exploratory data analys')
    st.write('by *josua simanjuntak*')

    #memasukkan gambar
    img = Image.open('gambar.jpg')
    st.image(img, caption="eda customer")
    
    #menulis baris
    st.write('## daftar pelanggan telco')


    #memasukkan data
    df = pd.read_csv(r"C:\Users\sonda\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")
    st.dataframe(df)


    #menampilkan histogram rating
    st.write('### diagram lingkaran Churn')
    jumlah = df["Churn"].value_counts()
    label = jumlah.index.map({'Yes':'Churn', 'No':'Tidak Churn', 1: 'Churn', 0:'Tidak Churn'})

    fig = plt.figure(figsize=(5,5))
    plt.pie(jumlah.values, labels=label, autopct='%1.1f%%', startangle=90,
            colors=['#7f7f7f' if l == 'Tidak Churn' else '#d62728' for l in label])
    plt.title('Perbandingan Pelanggan Churn dan Tidak Churn')
    st.pyplot(fig)

    #membuat
    st.write('### histogram berdasarkan input user')
    opsi = st.selectbox('Pilih kolom',('tenure','MonthlyCharges','TotalCharges'))

    fig = plt.figure(figsize=(15,5))
    sns.histplot(data=df, x=opsi, hue='Churn', bins=30, kde=True,
                 stat='density', common_norm=False)
    plt.title(f'Distribusi {opsi}: Churn vs Tidak Churn')
    st.pyplot(fig)




if __name__ == '__main__':
    run()    