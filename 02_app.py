from ssl import Options
import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.ensemble  import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
#Make container for the app
header=st.container()
data_sets=st.container()
features=st.container()
model_traning=st.container()
with header:
    st.title("kashti ki app")
    st.text("in this project we will work on kashti data")

with data_sets:
    st.header("kashti doob gaye")
    st.text("we will work on kashti data")
    #import data set:
    df=sns.load_dataset('titanic')
    # Dropping NAN values:
    df=df.dropna()
    st.write(df.head(10))
    st.subheader("Kithnay Aadmi Thy")
    st.bar_chart(df['sex'].value_counts())

    # Other Charts:
    st.subheader("Class k hisab sy faraq")
    st.bar_chart(df['class'].value_counts())
with features:
    st.header("These are our app features")
    st.text("Awen bht saray saray features add kartay hye, asaan hi hy?")
    st.markdown('1.**Feature 1:** This will tell us pata nhi kiya?')
    st.markdown('2.**Feature 2:** This will tell us pata nhi kiya?')
with model_traning:
    st.header("kashti waloo ka kya bna?- Model training")
    st.text(" اس میں ہم اپنے پیرامیٹرز کو بڑھا یا گھٹائیں گے۔")
    # Making Columns:
    input,display=st.columns(2)

    # Pehlay column main ap ki selection k points hun gyr
    max_depth=input.slider("How many people do you know ?", min_value=10 , max_value=100,value=20,step=5)


    # n_estimators
    n_estimators=input.selectbox("How many trees should be in a Random Forest?", options=[50,100,150,200,"No Limit"])
    
    #Adding list of features:
    input.write(df.columns)
    # Input Features from user:
    input_features=input.text_input("Which features we should use?")


    # Machine Learing Model:

    model=RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
    # Yahan per hum aik condition lagaye gay.
    if n_estimators=="No Limit":
        model=RandomForestRegressor(max_depth=max_depth)
    else:
        model=RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)
    # Define X(input) and Y(output):
    X=df[[input_features]]
    y=df[["fare"]]

    # Fit a Model:
    model.fit(X,y)
    pred= model.predict(y)


    # Display metrics:
    display.subheader("Mean absolute error of the model is: ")
    display.write(mean_absolute_error(y, pred))
    display.subheader("Mean squared error of the model is: ")
    display.write(mean_absolute_error(y,pred))
    display.subheader("R score error of the model is: ")
    display.write(r2_score(y,pred))
