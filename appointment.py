import streamlit as st
import plotly.graph_objs as go
import sqlite3
import pandas as pd

con = sqlite3.connect("DentalCabinet.db")
st.set_page_config(page_title='Shop Reports',page_icon=':bar_chart:',layout='wide')
#########################
#cur = con.cursor()
#cur.execute("SELECT name from sqlite_master WHERE type='table'")
#print(cur.fetchall())
#########################

query = "SELECT * FROM Appointment"
df = pd.read_sql_query(query,con)
copy_df = df.copy()
print(df)
print(len(df.Patient.unique()))


total_p = df.shape[0]
patient_number = len(df.Patient.unique())
doctor_number = len(df.Doctor.unique())

# Using st.markdown to apply styles to the text dynamically


# Create two columns with specific width ratios (e.g., 70% and 30%)
col1, col2, col3 = st.columns([0.4, 0.4,0.4])

with col1:
    bordered_text_html = f"""
<div style="border: 2px solid #4CAF50; padding-left: 15px; border-radius: 5px;">
    <h4 style="margin: 0; font-size:18px">Appointments</h4>
    <h1 style="margin: 0;">{total_p}</h1>
</div>
"""

    # Render the HTML in Streamlit
    st.markdown(bordered_text_html, unsafe_allow_html=True)

    
with col2:
    bordered_text_html = f"""
<div style="border: 2px solid #4CAF50; padding-left: 15px; border-radius: 5px;">
    <h4 style="margin: 0; font-size:18px">Patient</h1>
    <h1 style="margin: 0;">{patient_number}</h1>
</div>
"""

    # Render the HTML in Streamlit
    st.markdown(bordered_text_html, unsafe_allow_html=True)

with col3:
    bordered_text_html = f"""
<div style="border: 2px solid #4CAF50; padding-left: 15px; border-radius: 5px;">
    <h4 style="margin: 0; font-size:18px">Doctor</h4>
    <h1 style="margin: 0;">{doctor_number}</h1>
</div>
"""
    # Render the HTML in Streamlit
    st.markdown(bordered_text_html, unsafe_allow_html=True)


df['Date'] = pd.to_datetime(df['Date'])

cl1, cl2= st.columns([0.4,0.4])

df.set_index('Date',inplace=True)


monthly_data = df.resample('M').size()
print(len(monthly_data.values))



with cl1:
   with st.container():
   
    # Create the hollow pie chart with Plotly
    fig_pie = go.Figure(data=[go.Pie(labels=monthly_data.index.strftime('%B'), values=monthly_data.values, hole=.4)])
    fig_pie.update_layout(
    title_text='Monthly Data Distribution'
)
    st.plotly_chart(fig_pie)

# Display bordered text and pie chart inside the same container
patient_visit = df.groupby('Patient').sum()
print(patient_visit)












appoint_status = df.groupby('Status').size()
res_appointment_status =  appoint_status.reset_index()
res_appointment_status['Status'].replace({0:'open',1:'Failed',2:'Missed',3:'Completed'},inplace=True)




with cl2:
    fig_bar3 = go.Figure(data=[go.Bar(x=res_appointment_status.Status, y=res_appointment_status[0], marker_color='blue')])
    
    fig_bar3.update_layout(
       title_text='Appointment by Status',
        xaxis_title='Status',
        yaxis_title='Appoinment',

    )
    st.plotly_chart(fig_bar3)

copy_df['Date'] = pd.to_datetime(copy_df['Date'])
Nov = copy_df[(copy_df['Date'] > '2022-10-31') & (copy_df['Date'] < '2022-12-01')]

Nov['Status'].replace({0:'open',1:'Failed',2:'Missed',3:'Completed'},inplace=True)



Sep = copy_df[(copy_df['Date'] > '2022-08-31') & (copy_df['Date'] < '2022-10-01')]
#print(Sep['Status'].value_counts())
Sep['Status'].replace({0:'open',1:'Failed',2:'Missed',3:'Completed'},inplace=True)
#print(Sep['Status'].value_counts())

Oct = copy_df[(copy_df['Date'] > '2022-09-30') & (copy_df['Date'] < '2022-11-01')]
print(Oct['Status'].value_counts())

Oct['Status'].replace({1:'Failed',2:'Missed',3:'Completed'},inplace=True)
print(Oct['Status'].value_counts())
print(Oct['Status'].value_counts().index)




c1,c2,c3 = st.columns(3)

with c1:
    fig_bar2 = go.Figure(data=[go.Bar(x=Nov['Status'].value_counts().index, y=Nov['Status'].value_counts(), marker_color='blue')])
    
    fig_bar2.update_layout(
       title_text='Appointment Status November',
        xaxis_title='Status',
        yaxis_title='Appoinment',

    )
    st.plotly_chart(fig_bar2)

with c2:
    fig_bar4 = go.Figure(data=[go.Bar(x=Sep['Status'].value_counts().index, y=Sep['Status'].value_counts(), marker_color='blue')])
    
    fig_bar4.update_layout(
       title_text='Appointment Status September',
        xaxis_title='Status',
        yaxis_title='Appoinment',

    )
    st.plotly_chart(fig_bar4)

with c3:
    fig_bar5 = go.Figure(data=[go.Bar(x=Oct['Status'].value_counts().index, y=Oct['Status'].value_counts(), marker_color='blue')])
    
    fig_bar5.update_layout(
       title_text='Appointment Status October',
        xaxis_title='Status',
        yaxis_title='Appoinment',

    )
    st.plotly_chart(fig_bar5)

