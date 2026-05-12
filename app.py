import streamlit as st
import pandas as pd

try:
    path = r"C:\Users\Rudra\Desktop\cloud-kitchen-dashboard\kittchen-pnl-data.xlsx"
    df = pd.read_excel(path, header=1)
except:
    path = r"C:\Users\Rudra\Desktop\cloud-kitchen-dashboard\kittchen-pnl-data.xlsx"
    df = pd.read_excel(path, header=1)

tab1, tab2 = st.tabs(["📊 Kitchen Level PnL", "📈 Variance level PnL"])

with tab1:
    st.header("Kitchen Level PnL")
    st.write("This is where your data goes.")
    
    selected_store = st.selectbox("Select a Store:", options=df['CITY'].unique())


    filtered_df = df[df['CITY'] == selected_store]


    st.write(f"Showing results for: **{selected_store}**")
    st.dataframe(filtered_df)

with tab2:
    st.header("Variance level PnL")


