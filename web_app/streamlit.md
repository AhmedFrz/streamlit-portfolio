## Streamlit

### Description

- `streamlit` is a Python module that allows end users to solely create 'web applications' via Python code.

### Background Context

- `streamlit` started off as an open-source project (and still is) an open-source project that got acquired by `Snowflake`.

- The purpose of Streamlit is to make web development for any data-related application very accessible to any data analyst / data scientist.

### Installation and Setup

1. Ensure that you have a working virtual environment for Python.

- `conda`
- `venv`

2. Install `streamlit` by placing it in a `requirements.txt` file.

```txt
streamlit
```

3. Install the dependencies via `pip`.

```bash
pip install -r requirements.txt
```

4. Besides being able to use `streamlit` in a Python file, it also can be enabled from your `Terminal` through a command line interface by invoking the command `streamlit`.

#### Example - Hello World

```bash
streamlit hello
```

### Sample Application with Python Code

1. Create a Python file named `app.py`.

```python
import streamlit as st

# Create a title for the web page
st.title("Hello World")

# View text that says Hello, world.
st.text('Hello, world.')
```

2. Within the root where your `app.py` file is stored, you need to use the CLI to run the app.

```bash
streamlit run app.py
```

3. This will open a new tab in your browser on [location](http://localhost:8501)

### Advanced Usage

#### Widgets

- Widgets are interactive components that allow users to input data into your application.

- The best place to find all the possible widgets is the [documentation](https://docs.streamlit.io) page.

#### Custom Run Command

- Replace `[PORT]` with any port number which you want the Streamlit app to actually run on.

```bash
streamlit run app.py --server.port [PORT]
```