import numpy as np     
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from streamlit import markdown, pyplot     # this is code from sign_up_page.py file for important codes i want to use
from streamlit.delta_generator import DeltaGenerator

# Centering Functionality
def cetner_text(text:str, heading_type:int =1) -> DeltaGenerator:
    return markdown(f"<h{heading_type} style='text-align:center;'>{text} <h{heading_type}>", unsafe_allow_html=True)

"""
Graphing Calculator Utilities
"""

def plot_graph(equation: str, start_num: int, end_num: int, graph_color: str, num_points: int=1000) -> Figure:
    # Creating initial nummpy array
    x = np.linspace(start=start_num, stop=end_num, num=num_points)

    # Eval() - Convert the Python string into an executable Python code
    y = eval(equation)

    # Create a matplotlib graph
    fig = plt.figure(figsize=(10,10))

    plt.plot(x,y,color=graph_color)

    # Tell Streamlit to plot the graph
    pyplot(fig=fig)