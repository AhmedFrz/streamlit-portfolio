import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Custome Module
from streamlit_util import center_text

# Title 
center_text (text='Graphing Calculator App')

# Layout - Spec 3
column_one, column_two, column_three = st.columns(spec=3, gap='medium') # 3 coluimns bz we want 3 inputs

# Column_one  #starting num where you want graph start
with column_one:
    # Starting no for the graph
    start = st.number_input(label='Start', min_value=-1000, max_value=1000, value=-10)    #value here mean 'default value' inside the box
                                                                                        # and this will be insdie column one
    # Column_two  # ending num  where you want graph end
with column_two:
    # Ending number for the graph
    end = st.number_input(label='End', min_value=-999, max_value=999, value=10)

# Column_three #color of graph
    # Color picker
    color = st.color_picker(label="Pick a color")

# Text Area
# this area is where we can pass the equation

equation = st.text_area(label="type in an equation", placeholder="x**2")
##"label" leaving blank as we want to give example of an equation inside the box 
## so above equation wil give you string, how to turn that into a graph