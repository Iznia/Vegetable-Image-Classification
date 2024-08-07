# Import libraries
import eda, prediction
import streamlit as st

# Add sidebar
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Vegetable Image Classification'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write('''
This tool is designed to explore and predict vegetable images. It uses advanced data analysis and machine learning models to provide insights and predictions that can help in understanding and addressing vegetable image classification effectively.
''')

# Define the Home Page
def show_home():
    
    
    st.markdown('---')
     
    st.write('''
    This tool provides functionalities for Exploratory Data Analysis and Prediction regarding vegetable image classification. 
    Use the navigation pane on the left to select the module you wish to utilize.
    ''')
    
    # Dataset
    st.write('#### 📈 Dataset')
    st.markdown('''
    The dataset contains pertinent information on various vegetable images. It includes images of Cabbage, Capsicum, Carrot, Cauliflower, and Pumpkin.
    ''')
    
    # Problem Statement
    st.write('#### ⚠️ Problem Statement')
    st.markdown('''
    The challenge is to accurately classify different types of vegetables from images. This classification task can help in various applications such as automated sorting, inventory management, and enhancing user experiences in agriculture-related applications.
    ''')    
    
    # Objective
    st.write('#### 💡 Objective')
    st.markdown('''
    The goal of this project is to create a `Convolutional Neural Network (CNN)` model that accurately predicts the type of vegetable from images. It will distinguish between **Cabbage**, **Capsicum**, **Carrot**, **Cauliflower**, and **Pumpkin**, primarily using `accuracy` as the evaluation metric. This aims to improve classification accuracy and assist in various practical applications.
    ''')

# Create condition to access different pages
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Vegetable Image Classification':
    prediction.run()
