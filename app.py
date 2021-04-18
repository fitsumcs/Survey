import pandas as pd 
import streamlit as st 
import plotly.express as px 
from PIL import Image 

# Set page title 
st.set_page_config(page_title="Survey Data")
st.header('Survey Result of 2022')

# Load Data from excel to dataframe 
ex_file = 'Survey.xlsx'
sheet_name = 'DATA'
data_frame_survey = pd.read_excel(ex_file, 
                  sheet_name= sheet_name,
                  usecols='B:D',
                  header= 3
                  )
# participant's 
data_frame_participant = pd.read_excel(ex_file, 
                  sheet_name= sheet_name,
                  usecols='F:G',
                  header= 3
                  )

# Display df 
st.dataframe(data_frame_survey)


# Chart of participant 
piChart = px.pie(data_frame_participant,
           title="Total Number of Participants",
           values='Participants',
           names='Departments'
           )
# Plot the chart 
st.plotly_chart(piChart)
