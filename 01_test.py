import streamlit as st
import seaborn as sns
st.header("This video is brought to you by Baba Ammar")
st.text("This is a simple demo of Streamlit")
st.header("Pata nhi kya likhna hy?")
df=sns.load_dataset('iris')
st.write(df.head())
st.write(df[['species','sepal_length','petal_length']].head())
st.bar_chart(df['sepal_length'])
st.line_chart(df['sepals_length'])