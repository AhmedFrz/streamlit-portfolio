# What is this file for?
# This is for storing functions 
# which are used frequently and by storing those functions here, we reduce redundancy 

# from streamlit import markdown or from streamlit import markdown---both are correct for return function to work
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

# Centering Functionality
#we borrowed "center_text" it from signup page

def center_text(text: str, heading_type: int = 1) -> DeltaGenerator:   
    return st.markdown(f"<h{heading_type} style='text-align: center;' >{text}</h{heading_type}>", unsafe_allow_html=True)


""" Graphing Calculator Utilities """
import numpy as np                       
from matplotlib.figure import Figure    

# assuming we have an equation which is str
# also we 3 inputs, start no, end no


def plot_graph (equation: str, start_num:int, end_num: int, num_points=1000) -> Figure:
    
def plot_graph (equation: str, start_num:int, end_num: int, num_points:int =1000) -> Figure:
    # Creating your initial numpy array
    x = np.linspace(start=start_num, end=end_num, num=1000)