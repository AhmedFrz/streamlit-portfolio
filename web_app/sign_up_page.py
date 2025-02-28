import streamlit as st
from streamlit.delta_generator import DeltaGenerator

# Custom Module
from streamlit_util import center_text

# Title
center_text('Sign up page')

# Sign up form
column_one, column_two = st.columns(spec=2, gap="medium")

with column_one:
    # Username
    username = st.text_input(label="", placeholder="username")

    # Password
    password = st.text_input (label = "", placeholder = "password", type = "password") 

with column_two:
    # Email
    email = st.text_input (label = "", placeholder = "email")

    # How about adding option to upload and preview images

    # File Uploaded Widget
    profile_photo = st.file_uploader(label = "Upload a profile photo", type = ['png', 'jpg', 'jpeg'] )

# Adding Preview button
if st.button(label= "submit "):
    
    # setup previews
    center_text(text=f'Hello, {username}', heading_type = 3)

    # Display the photo 
    st.image(image = profile_photo)    
