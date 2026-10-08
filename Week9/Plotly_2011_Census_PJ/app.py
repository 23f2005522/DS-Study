import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

df= pd.read_csv("./data/india.csv")

list_of_states = df['State name'].unique().tolist()
list_of_states.insert(0,"All States")





st.dataframe(df)


st.sidebar.title("India Census 2011 Data Analysis")
selected_state = st.sidebar.selectbox("select a state",list_of_states)


