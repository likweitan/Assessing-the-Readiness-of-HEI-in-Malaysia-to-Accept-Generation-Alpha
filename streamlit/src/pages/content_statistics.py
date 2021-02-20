import streamlit as st
import altair as alt

import pandas as pd
import numpy as np


def load(data):
    st.title('🎲 Course Statistics')

    chart = plot_play_count_graph(data[0])

    col1,col2=st.beta_columns(2)

    with col1:
        st.write('> **Course Analytics**')
        with st.spinner('Loading graph...'):
            st.altair_chart(chart, use_container_width=True)

@st.cache(persist=True, show_spinner=False,allow_output_mutation=True)
def plot_play_count_graph(info_content_df: pd.DataFrame):
    chart = alt.Chart(info_content_df).mark_bar().encode(
        x='count()',
        y='learning_stage',
        color='difficulty',
        order=alt.Order(
            # Sort the segments of the bars by this field
            'learning_stage',
            sort='ascending'
        )

    ).properties(
        width=1500,
        height=200
    )
    return chart

    


def plot_connect():
    st.write('aa')

