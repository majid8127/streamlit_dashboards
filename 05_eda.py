import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns

# Webapp ka title:
st.markdown('''
# **Exploratory Data Analysis Web Application**
This app is developed to perform exploratory data analysis on a dataset.
 ''')

# How to upload a fiel from your computer:

with st.sidebar.header("Upload a file(.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload a file", type=["csv", "txt"])
    df=sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/streamlit/streamlit/master/examples/data/iris.csv)")
    
    #profiling report for pandas:

if uploaded_file is not None:

    def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv
    df=load_csv()
    pr=ProfileReport(df,explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file, upload ker  do ab ya kaam nahi lena?')
    if st.button('Press to use example data'):
       #example data:


      def load_data():
          a=pd.DataFrame(np.random.randn(100,5),
                       columns=['age','banana','codanics','deutchland','Ear'])
          return a
    df=load_data()
    pr=ProfileReport(df,explorative=True)
    st.header("**Input DF**")
    st.write(df)
    st.write('---')
    st.header('**Profiling Report with pandas**')
    st_profile_report(pr)
 
