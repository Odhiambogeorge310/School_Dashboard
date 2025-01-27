#Loading necessary libraries
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as xp

#loading dataset
@st.cache_data
def get_data():
    df=pd.read_csv("learners.xls")
    return df


#converting data into dataframe
st.dataframe(df)

#Building sidebar
st.sidebar.title("Please Filter Here")

#Gender sidebar
st.sidebar.radio("Select_Gender:",options=df['GENDER'])

#citizenship sidebar
st.sidebar.radio("Select_citizenship:",options=df['CITIZENSHIP'])

#Gender sidebar
st.sidebar.radio("Select_Gender:",options=df['GENDER'])