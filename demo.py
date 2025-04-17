import streamlit as st
import pandas as pd

st.title("🚀 My First Streamlit Dashboard")

data = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas'],
    'Sales': [100, 80, 130]
})

st.subheader("📊 Sales Chart")
st.bar_chart(data.set_index('Fruit'))
