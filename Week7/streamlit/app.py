import streamlit as st
import pandas as pd
import time


st.title("Startup Dashboard App")
st.header("Welcome to the Startup Dashboard!")
st.subheader("This app provides insights into startup performance and metrics.")
st.write("Use the sidebar to navigate through different sections of the dashboard.")

st.header("Welcome to the Startup Dashboard!2")
st.subheader("This app provides insights into startup performance and metrics.2")
st.write("Use the sidebar to navigate through different sections of the dashboard.")

st.markdown("""
            ### Features
            - View key performance indicators (KPIs) for your startup.
            - Analyze financial metrics and growth trends.
            - Visualize data through interactive charts and graphs.
            ```python
            import pandas as pd
            import numpy as np
            ```
            """)

st.code("""
import pandas as pd
import numpy as np

def load_data():

    # Load your startup data here
    data = pd.read_csv('startup_data.csv')
    return data
""", language='python')

st.latex("E = mc^2", width=200)

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'package' : [1000, 2000, 3000, 4000]
}

df = pd.DataFrame(data)


st.dataframe(df)

st.write("Use the sidebar to navigate through different sections of the dashboard.")
st.metric("Revenue", value = "$1,000,000", delta = "-5%" , border=True)


st.json(
    data
)



### showiwing media

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj-KE_MT_-hQyVM7DHVPneFLHh5FLq7qTRvgvarO4M1w&s" , width=300)


st.video("https://www.youtube.com/watch?v=kVKG-mYqx7Q")




## creatinglayouts -sidebar , columns , tabs


st.sidebar.title("Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("This is the first column.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj-KE_MT_-hQyVM7DHVPneFLHh5FLq7qTRvgvarO4M1w&s" , width=300)
    
    
    
with col2:
    st.header("Column 2")
    st.write("This is the second column.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj-KE_MT_-hQyVM7DHVPneFLHh5FLq7qTRvgvarO4M1w&s" , width=300)
    
    
    
with col3:
    st.header("Column 3")
    st.write("This is the third column.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj-KE_MT_-hQyVM7DHVPneFLHh5FLq7qTRvgvarO4M1w&s" , width=300)
    
    
st.success("This is a success message.")
st.info("This is an info message.")
st.warning("This is a warning message.")
st.error("This is an error message.")



## progress bar

# bar = st.progress(0)

# for percent_complete in range(100):
#     time.sleep(0.05)
#     bar.progress(percent_complete + 1)
    
    
## Taking user Input 
name  =  st.text_input("Enter your name:")
number = st.number_input("Enter a number:", min_value=0, max_value=100, step=1)
date = st.date_input("Select a date:")

## Dropdown and multiselect
option = st.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])
multi_option = st.multiselect("Select multiple options:", ["Option A", "Option B", "Option C", "Option D"])

## buttons and checkboxes
id = st.text_input("Enter your ID:")
password = st.text_input("Enter your password:", type="password")

btn = st.button("Submit")


if btn:
    st.write(f"Name: {name}")
    st.write(f"Number: {number}")
    st.write(f"Date: {date}")
    st.write(f"ID: {id}")
    st.write(f"Password: {password}")    
    st.write(f"Selected option: {option}")
    st.write(f"Selected multiple options: {multi_option}")
    if name == "Anish" and password == "1234":
        st.success("Login successful!")
        st.balloons()
    else:
        st.error("Invalid credentials. Please try again.")
        
        
### uploading files

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt"])

if uploaded_file is not None : 
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    st.dataframe(df.describe())
