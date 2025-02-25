import streamlit as st

from streamlit.delta_generator import DeltaGenerator

def center_text(text: str, heading_type: int = 1) -> DeltaGenerator:   #here, we changed center text to have default parameters
                                                                 ## i.e. heading_type=3
    return st.markdown(f"<h{heading_type} style='text-align: center;' >{text}</h{heading_type}>", unsafe_allow_html=True)


# Title
center_text('Sign up page')

# Sign up form

# Username
username = st.text_input(label="", placeholder="username")

# Password
password = st.text_input (label = "", placeholder = "password", type = "password") 

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
