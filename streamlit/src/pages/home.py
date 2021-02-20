import streamlit as st
import altair as alt
import plotly.express as px

import pandas as pd
import numpy as np

def load(data) -> None:
    """ The homepage is loaded using a combination of .write and .markdown.
    Due to some issues with emojis incorrectly loading in markdown st.write was
    used in some cases.
    When this issue is resolved, markdown will be used instead.
    """
    # st.image("https://raw.githubusercontent.com/MaartenGr/boardgame/master/images/logo_small.jpg",
    #         use_column_width = True)
    st.title('Assessing the Readiness of HEI in Malaysia to Accept Generation Alpha')
    
    month_student=get_student_month(data[1])
    month_content=get_active_content(data[0],data[2])
    ready_student=get_ready_student(data[1],data[2])
    city_student=get_city_student(data[1])

    col1, col2, col3 = st.beta_columns([2,2,3])

    with col1:
        st.write('> **Total Number of Student Enrolled**')
        st.write('# '+""+str(data[1].shape[0]))
        st.write('There are **'+str(month_student)+'** student increased compared to previous day.')
    
    with col2:
        st.write('> **Total Number of Problem Attempted**')
        st.write('# '+str(data[2].shape[0]))
        st.write('There are **'+str(month_content)+'** new problems attempted compared to previous month.')
    
    with col3:
        st.write('> **Readiness of Students**')
        bar_chart=alt.Chart(ready_student).mark_bar().encode(
            alt.X('count'),
            y='readiness',
            color='readiness'
        ).properties(
            height=175
        )
        st.altair_chart(bar_chart,use_container_width=True)

    st.write("")

    col1, col2 = st.beta_columns([4,3])

    with col1:
        st.write('> **Problems Attempted History**')
        #st.multiselect('ss',['Overall','Specified'])

        with st.spinner('Loading graph...'):
            datecount_df = plot_play_count_graph(data[0], data[1], data[2])
            st.write('From the chart below, we could see that the number of users attempt the question is getting lower.')
            chart = alt.Chart(datecount_df).mark_line().encode(
                x='date',
                y='count'
            )
        st.altair_chart(chart, use_container_width=True)
    
    with col2:
        st.write('> **User City Distribution**')
        st.write('The city distribution')
        bar_chart=alt.Chart(city_student).mark_bar().encode(
            alt.X('city'),
            y='count',
            color='city'
        )
        st.altair_chart(bar_chart,use_container_width=True)

@st.cache(persist=True, show_spinner=False)
def get_student_month(info_userdata_df: pd.DataFrame):
    info_userdata_df['first_login_date_TW'] = pd.to_datetime(info_userdata_df['first_login_date_TW'], format='%Y-%m-%d')
    info_userdata_df = info_userdata_df.rename(columns = {'first_login_date_TW':'date_login'})
    month_student = info_userdata_df['date_login'].value_counts(ascending=True)
    return month_student[0]

@st.cache(persist=True, show_spinner=False)
def get_active_content(info_content_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    log_problem_df['x'] = pd.to_datetime(log_problem_df['timestamp_TW'], format='%Y-%m-%d %H:%M:%S %Z').dt.date
    log_problem_df = log_problem_df.rename(columns = {'x':'date_attempt'})
    merge_df=info_content_df.merge(log_problem_df, how='inner', on='ucid')
    month_content = merge_df['date_attempt'].value_counts().sort_index()
    return month_content[0]

@st.cache(persist=True, show_spinner=False)
def plot_play_count_graph(info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    datecount_df = (pd.to_datetime(log_problem_df['timestamp_TW'], format='%Y-%m-%d %H:%M:%S %Z')
                    .dt.floor('d')
                    .value_counts()
                    .rename_axis('date')
                    .reset_index(name='count')
                    .sort_values('date'))

    
    return datecount_df;

@st.cache(persist=True, show_spinner=False)
def get_ready_student(info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    merge_df=info_userdata_df.merge(log_problem_df, how='inner', on='uuid')
    x=merge_df.groupby(by=['uuid','ucid']).agg({'level': 'max'}).reset_index()
    y=x.groupby(by=['uuid']).agg({'level':'mean'}).round()
    bins=[-1,2,5]
    labels=['Not ready','Ready']
    y['readiness']=pd.cut(y['level'], bins,labels=labels)
    y['readiness']=y['readiness'].astype(object)
    ready_student=y['readiness'].value_counts().rename_axis('readiness').reset_index(name='count')
    return ready_student

@st.cache(persist=True, show_spinner=False)
def get_city_student(info_userdata_df: pd.DataFrame):
    city_student=info_userdata_df['user_city'].value_counts().rename_axis('city').reset_index(name='count')
    return city_student