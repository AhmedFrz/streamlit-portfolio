
import streamlit as st

# 9.
from streamlit.delta_generator import DeltaGenerator

# 8. Centering Functionality
    # def center_text(text: str) -> DeltaGenerator:
    #     return st.markdown(f"<h1 style='text-align: center;' >{text}</h1>", unsafe_allow_html=True)


# 10. Changing  8.
def center_text(text: str, heading_type: int = 1) -> DeltaGenerator:   #here, we changed center text to have default parameters
                                                                 ## i.e. heading_type=3
    return st.markdown(f"<h{heading_type} style='text-align: center;' >{text}</h{heading_type}>", unsafe_allow_html=True)

# Notice font size is different after we submit the pic

# 1. Title
# st.title("sign up page")

# 9. Title
center_text('Sign up page')


# 2. Sign up form

# 3. Username
# username = st.text_input(label = "username")

username = st.text_input(label="", placeholder="username")


# 4. Password
# password = st.text_input (label = "password")   #shows outiside on box
#password = st.text_input (label = "", placeholder = "password") # but if you type, it shows pass
password = st.text_input (label = "", placeholder = "password", type = "password")  #encrypted

# 5. Email
email = st.text_input (label = "", placeholder = "email")


# How about adding option to upload and preview images

# 6. File Uploaded Widget

profile_photo = st.file_uploader(label = "Upload a profile photo", type = ['png', 'jpg', 'jpeg'] )

# 7. We shoul have preview button when we hit submit

if st.button(label= "submit "):  # i.e. if someone clicks the button 
    
    # setup previews
    # st.markdown(f"Welcome, {username}")
    # 11. 
    center_text(text=f'Hello, {username}', heading_type = 3)

    # Display the photo 
    st.image(image = profile_photo)    #in this widget, you can pass image, & it will preview it
    

    # f-string = stands for format
    # converts var which might not be a string