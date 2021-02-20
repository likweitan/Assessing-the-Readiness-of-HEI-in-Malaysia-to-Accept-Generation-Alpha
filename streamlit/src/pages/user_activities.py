from altair.vegalite.v4.schema.core import Scale
import streamlit as st
import altair as alt
import plotly.express as px

import pandas as pd
import numpy as np


def load(data):
    st.title('🎲 User Statistics')
    st.sidebar.header('User')
    user = st.sidebar.selectbox('Please select an user', ['Student A','Student B','Student C','Student D','Student E'])
    switcher = {
        'Student A': "Kpq2q+eKw/O+6/jLs3XJosgmI7weEJxJZdnkKTbbF8I=",
        'Student B': "0+VU/Zb0Q96uoByuRhl7r9bJuJO6CKWpsmNMEuijSzc=",
        'Student C': "g8DnYvIqpolw10XlwWeIWv6NbDPByUbmgH8EshJqBns=",
        'Student D': "kSyUTFlepsYUD723IPL/jEZ520xaKbscrBmNtBUFR1o=",
        'Student E': "XMFbFA7C49+LRhUddhelfPpA6F5dbOoxeyL3eYbuTlY="
    }
    user_id = switcher.get(user,"Invalid")

    st.write('**Student ID: **'+user_id)
    st.write('The following table shows the subjects that users have attempted')
    merge_df = merge_all(data[0], data[1], data[2])
    course = merge_df[['ucid','problem_number','total_sec_taken','level']][merge_df['uuid']==user_id]
    grouped_course = course.groupby(by=['ucid']).agg({'problem_number':'max','total_sec_taken':'mean','level':'max'}).reset_index()
    
    col1, col2 = st.beta_columns([5,2])

    with col1:
        st.line_chart(grouped_course,height=450)
    
    

    line_plot = alt.Chart(grouped_course).mark_bar().encode(
        x='ucid',
        y='level',
        color=alt.condition(
        alt.datum.level > 2,
        alt.value("green"),  # The positive color
        alt.value("red")  # The negative color
        )
    ).properties(height=400)
    
    st.altair_chart(line_plot, use_container_width=True)

    with st.beta_expander("More"):
        st.table(grouped_course)
    st.write(grouped_course['level'].value_counts().reset_index())
    
    fig = px.pie(grouped_course, values=grouped_course['level'].value_counts(), names=grouped_course['level'].value_counts().index, color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"],title='Percentage')
    
    with col2:
        st.plotly_chart(fig, use_container_width=True)


@st.cache(show_spinner=False)
def merge_all(info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    merge_df = log_problem_df.merge(info_userdata_df, how='left', on='uuid')
    merge_df = merge_df.merge(info_content_df, how='left', on='ucid')
    return merge_df