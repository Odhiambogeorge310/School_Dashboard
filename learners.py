
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
#import matplotlib.pyplot as plt

#st.set_page_config(page_title="IMACULATE_SCHOOL_DASHBOARD", page_icon=":mechanical_arm:", layout="wide")
#....................................................................................................
# loading dataset
@st.cache_data
def get_data():
    data = pd.read_excel('learners.xlsx')
    return data
#...................................................................................................
# invoking the function
data = get_data()

#..................................................................................................

# Building sidebar
st.sidebar.header('Please Filter Here')

# gender sidebar
gender=st.sidebar.radio("Select_Gender", options=data['GENDER'].unique())

# Grade sidebar
grade=st.sidebar.multiselect("Select_Grade:", options=data["GRADE"].unique(),default=data["GRADE"].unique())


#Stream sidebar
stream = st.sidebar.multiselect('Select_Stream:', options = data['STREAM'].unique(), default = data['STREAM'].unique())

#........................................................................................................................
#linking database
df_select = data.query(
    "GENDER== @gender & STREAM==@stream & GRADE==@grade"
)

#........................................................................................................................
#warning
if df_select.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() ##-- halt streamlit from further execution

#.......................................................................................................................
#main page title
st.title("🎓IMMACULATE_SCHOOL_DASHBOARD")
st.markdown("##")



st.divider()
#......................................................................................................................
#calculate KPIs
Girls_count = df_select.loc[df_select['GENDER'] == 'Girl'].count()[0]
Boys_count = df_select.loc[df_select['GENDER'] == 'Boy'].count()[0]
Total_count=df_select.loc[df_select['GENDER'] == 'Boy'].count()[0]
Total_count=df_select.loc[df_select['GENDER'] == 'Girl'].count()[0]
pop=(Girls_count+Boys_count)

#.......................................................................................................................

#first_partition
first_column, second_column, third_column=st.columns(3)

with first_column:
    st.subheader("🧍‍♀️Girls_Count:")
    st.subheader(f"{Girls_count}")


with second_column:
    st.subheader("🧍Boys_Count:")
    st.subheader(f"{Boys_count}")

with third_column:
    st.subheader("Total_Count:")
    st.subheader(f"{pop}")
#.............................................................................................................................
st.divider()

#second_partition
#............................................................................................................................
#citizenship sidebar
citizenship = st.sidebar.radio('Choose Citizenship:', options = data['CITIZENSHIP'].unique())
df_select = data.query(
    "CITIZENSHIP == @citizenship"
)

#Calculating_kpis
citizens = df_select.loc[df_select['CITIZENSHIP'] == 'CITIZEN'].count()[0]
foreigner = df_select.loc[df_select['CITIZENSHIP'] == 'FOREIGNER'].count()[0]

#general Distribution
Girl = df_select.loc[df_select['GENDER'] == 'Girl'].count()[0]
Boy = df_select.loc[df_select['GENDER'] == 'Boy'].count()[0]
#color=['#eb34c0',"#4b5beb"]
data = {'Gender': ['Boy', 'Girl'],
        'Count': [Boy, Girl]}  

# Create a DataFrame 
gender = pd.DataFrame(data)

# Create a pie chart using plotly express
fig = px.pie(gender, names='Gender', values='Count', title='General_Distribution')

fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False)))


first_column,second_column,third_column=st.columns(3)

with first_column:
    st.subheader("Citizens_Count:")
    st.subheader(f"{citizens}")


with second_column:
    st.subheader("Foreigners_Count:")
    st.subheader(f"{foreigner}")
#...................................................................................................................................................................................................................
st.divider()
#Third_partition
#gender sidebar
grade=st.sidebar.radio("Select_Grade:",options=df_select['GRADE'].unique())

#linking database
df_select = df_select.query(
    "GRADE==@grade"
)

# pie_chart
gender_count=df_select['GENDER'].value_counts().reset_index()
gender_count.columns = ['GENDER', 'count']
# Define a custom color sequence
color_sequence = ["#eb34c0","#4b5beb"]
labels = ['BOYS','GIRLS']

pie = px.pie(gender_count, values='count', names='GENDER',color='GENDER', labels=labels, title="Distribution_Per_Grades",
             color_discrete_sequence=color_sequence)
#st.plotly_chart(pie)

#Histogram
#color = ["#4b5beb","#eb34c0"]
custom_colors = {
    'Boys': 'blue',   # Color for boy
    'Girl': 'pink'  # Color for girl
}


bar=px.histogram(df_select, x='GENDER', title='Hist_Gender_Distribution', color="GENDER",color_discrete_map=custom_colors)
#st.plotly_chart(bar)



left_column, middle_column,right_column=st.columns(3)
left_column.plotly_chart(pie, use_container_width=True)
middle_column.plotly_chart(fig, use_container_width=True)
right_column.plotly_chart(bar, use_container_width=True)
#......................................................................................................................................................................
st.divider()

#creating dataframe
st.dataframe(df_select)
