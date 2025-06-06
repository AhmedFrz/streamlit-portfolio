import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from os import getcwd, listdir
from os.path import splitext
import os
import json

# Custom Modules
from streamlit_util import center_text
from report_util import generate_report, export_to_html
from database_util import load_db_variables, create_postgres_engine, create_postgres_connection

# Streamlit App
center_text("Data Quality Web App")

# Create a sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose the app mode", ["Data Upload", "SQL Query"])

# Initialize engine variable
engine = None

# DB Connection - Run this code only once at the start
if 'db_variables' not in st.session_state:
    # Path to our JSON File
    json_path = os.path.join(getcwd(), "postgres_creds.json")

    # Load DB Variables from JSON
    with open(json_path, 'r') as f:
        db_variables = json.load(f)

    st.session_state.db_variables = db_variables

if 'engine' not in st.session_state:
    # Create Postgres Engine with explicit arguments
    engine = create_postgres_engine(
        username=st.session_state.db_variables['POSTGRES_USER'],
        password=st.session_state.db_variables['POSTGRES_PASSWORD'],
        host=st.session_state.db_variables['POSTGRES_HOST'],
        port=st.session_state.db_variables['POSTGRES_PORT'],
        database=st.session_state.db_variables['POSTGRES_DATABASE']
    )
    st.session_state.engine = engine

engine = st.session_state.engine

# Tabs - Separate File Upload from SQL Query
tab_one, tab_two = st.tabs(["File Upload", "SQL Query"])

with tab_one:

    # Upload File
    uploaded_file = st.file_uploader("Choose a file", type=['csv'])

    # Preview your data
    if uploaded_file is not None:
        # Reading the CSV as a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Streamlit widget to preview DataFrames
        st.dataframe(df)

        st.write(df.shape)

        # Button to upload CSV to database
        if st.button("Upload CSV to Database"):
            df.to_sql('youtube_videos', engine, if_exists='replace', index=False)
            st.success("CSV uploaded to database as table 'youtube_videos'.")
    
    # Path to where the report should be saved
    report_path = getcwd() + "/html_assets"
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    # Button - Generate Report
    if st.button("Generate Report"):
        # File Name
        file_name = uploaded_file.name

        # File Name without the extension
        file_name = splitext(file_name)[0]

        # Report Name
        report_name = f'{file_name}.html'

        if df.empty:
            st.warning("The uploaded file is empty. Please upload a non-empty CSV file.")
        else:
            # Control Flow
            if report_name not in listdir(report_path):
                # Generate report
                report = generate_report(df)
                # Export to HTML
                export_to_html(report=report, file_path= os.path.join (report_path, report_name))
            # Render the HTML
            report_full_name = os.path.join(report_path, report_name)
            with open(report_full_name, encoding="utf-8") as f:
                html = f.read()
                components.html(html, height=800, width=800, scrolling=True)

with tab_two:
    # Markdown
    st.markdown("### SQL Query to DataFrame")

    # Text Area
    sql_query = st.text_area("Enter your SQL Query: ")

    # Button - Execute Query
    if st.button("Execute Query"):
        # Establish the connection as a context manager
        with create_postgres_connection(engine) as conn:
            # Execute the query
            df = pd.read_sql_query(sql=sql_query, con=conn)
        
        # # Close the connection
        # conn.close()

        # Display the DataFrame
        st.dataframe(df)

        if df.empty:
            st.warning("The DataFrame is empty. Please provide a non-empty result.")
        else:
            profile = generate_report(df)
            st.subheader("Data Report")
            html_report = profile.to_html()
            # Use Streamlit's HTML rendering function
            st.components.v1.html(html_report, height=2000, width=800)


