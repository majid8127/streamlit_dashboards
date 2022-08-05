
import streamlit as st
import plotly.express as px
import pandas as pd



# Import dataset:
st.title("Plotly and Streamlit ko mila k app banani hy")
df=px.data.gapminder()   #gapminder is the name of dataset.
st.write(df)
st.write(df.head())      #It will show the head of dataset.
st.write(df.columns)     #it will show just name of columns.

# Summary Statistics:
st.write(df.describe())   #It will show mean,median,std etc,

# data management:
#The following code shows that take the unique values of year column.
year_option=df['year'].unique().tolist()
# the command "tolist()" shows convert it into list.
#With the "st.selectbox" we create a box and with "year_option"
# It will take values of year_optionn in that box.
year=st.selectbox('Which year should we plot?',year_option,0)

# df=df[df['year']==year]

#plotting by country and year:
st.subheader('Animated Graph by country and year')
fig=px.scatter(df, x='gdpPercap', y='lifeExp', size='pop',color='country', hover_name='country',
                log_x=True, size_max=55, range_x=[100,100000],range_y=[20,90],
                animation_frame='year',animation_group='country')
#In the previous code 'x' and 'y' are columns,size='pop' means size of graph 
# should be changed according to population.
# color='countary' means color should be change according to country.
# hover_name='country' means when we move curser on graph the
# country name should be appeared on cursor.
#Log_x=True is used for normalized data.
# range of x and y should ranges of both.

st.write(fig)

#plotting by country and year:
st.subheader('Animated Graph by continent and year')
fig=px.scatter(df, x='gdpPercap', y='lifeExp', size='pop',color='continent', hover_name='country',
                log_x=True, size_max=55, range_x=[100,100000],range_y=[20,90],
                animation_frame='year',animation_group='continent')
st.write(fig)

#plotting by country and year:
st.subheader('Animated Graph by continent and year')
fig=px.scatter(df, x='gdpPercap', y='lifeExp', size='pop',color='pop', hover_name='country',
                log_x=True, size_max=55, range_x=[100,100000],range_y=[20,90],
                animation_frame='year',animation_group='pop')
st.write(fig)