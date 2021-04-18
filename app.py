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

# Drop the null  values 
data_frame_participant.dropna(inplace=True)



# Chart of participant 
piChart = px.pie(data_frame_participant,
           title="Total Number of Participants",
           values='Participants',
           names='Departments'
           )


# Display select selection 
department = data_frame_survey['Department'].unique().tolist()
ages = data_frame_survey['Age'].unique().tolist()

age_filter = st.slider('Age ', 
                     min_value=min(ages),
                     max_value=max(ages),
                     value=(min(ages),max(ages))
                     )
# Department filter 
department_filter = st.multiselect  ('Department: ', 
                     department,
                     default=department,
                     )

# Creating filter 
mask = (data_frame_survey['Age'].between(*age_filter)) & (data_frame_survey['Department'].isin(department_filter))
result = data_frame_survey[mask].shape[0]
st.markdown(f'* Number of Survey Takes : {result} *')




# Display df 
st.dataframe(data_frame_survey)
# Plot the chart 
st.plotly_chart(piChart)

