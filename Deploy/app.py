
 # Import required libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

 # Load the trained model from pickle file
pickle_in = open("Deploy/crop.pkl","rb")
final_model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "--Welcome--"

# Define a function for predicting crop yield
#@app.route('/predict',methods=["Get"])
def predict_rating(Rainfall, Temperature,Country_Burundi,Country_Comoros, Country_Eritrea,Country_Madagascar,Country_Mauritius,Country_Mozambique,Country_Uganda,Item_Barley,Item_Ginger,Item_Hops,Item_Maize,Item_Oats,Item_Potatoes,Item_Wheat):
    
    input_data = [Rainfall, Temperature,Country_Burundi,Country_Comoros, Country_Eritrea,Country_Madagascar,Country_Mauritius,Country_Mozambique,Country_Uganda,Item_Barley,Item_Ginger,Item_Hops,Item_Maize,Item_Oats,Item_Potatoes,Item_Wheat]
    
    input_data = np.reshape(input_data, (1, -1))

    prediction=final_model.predict(input_data)
    print(prediction)
    return prediction

 # Define a function for the Streamlit app
def main():
     # Set up the Streamlit app title and header
    st.set_page_config(page_title="Crop Yield Predictor ML Model", 
                       page_icon=":bar_chart:", 
                       layout="wide")
    st.title("Crop Yield Predictor ML Model")
    
    # Add a menu icon in the top right corner
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    # Display different pages based on menu choice
    if choice == "Home":
        home_page()
    elif choice == "About":
        about_page()

# define a function for the home page
def home_page():
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">CROP YIELD PREDICTOR FOR EAST AFRICAN COUNTRIES ML APP </h2>
    <style>body{background-color: #FFFFFF;}</style>
    </div>

    <div>
        <p style="color:white;text-align:center;"> >>    Rainfall is represented in mm. For Example for rainfall input 0.78. </p>
        <p style="color:white;text-align:center;"> >>    Temperature is represented in celisus. For Example for Temperature input 0.68. </p>
    </div>
    """
    image = Image.open("cr3.jpg")   # Update the file path with your actual image file path
    st.image(image, caption='Crop Cultivation', use_column_width=True)
    st.markdown(html_temp,unsafe_allow_html=True)

    """ >> Please Input Values Below To Access The Predictor:
    """

    #Error Handeling 
    try:
        Rainfall = st.text_input("Rainfall")
        Temperature = st.text_input("Temperature")
        Country_Burundi = st.text_input("Country_Burundi")
        Country_Comoros = st.text_input("Country_Comoros")
        Country_Eritrea = st.text_input("Country_Eritrea")
        Country_Madagascar = st.text_input("Country_Madagascar")
        Country_Mauritius = st.text_input("Country_Mauritius")
        Country_Mozambique = st.text_input("Country_Mozambique")
        Country_Uganda = st.text_input("Country_Uganda")
        Item_Barley = st.text_input("Item_Barley")
        Item_Ginger = st.text_input("Item_Ginger")
        Item_Hops = st.text_input("Item_Hops")
        Item_Maize = st.text_input("Item_Maize")
        Item_Oats = st.text_input("Item_Oats")
        Item_Potatoes = st.text_input("Item_Potatoes")
        Item_Wheat = st.text_input("Item_Wheat")
    except Exception as e:
        # Handle any exceptions that may occur during prediction
        st.error("Error occurred: Please enter a vaild input {}".format(e))
    
    result = 0
    if st.button("Predict"):
        # Call the prediction function with input data
        result=predict_rating(float(Rainfall),float(Temperature),int(Country_Burundi),int(Country_Comoros)
                              ,int(Country_Eritrea),int(Country_Madagascar),int(Country_Mauritius),
                              int(Country_Mozambique),int(Country_Uganda),int(Item_Barley),
                              int(Item_Ginger),int(Item_Hops),int(Item_Maize),int(Item_Oats),int(Item_Potatoes),int(Item_Wheat))
    st.success(' => The Predicted crop yield is {} (hg/ha).' .format(str(result)))
    """
    "hg/ha" typically refers to the amount of produce (such as crops or fruits) harvested per hectare of land.
    
    """
 # define a function for the about page  
def about_page():
    html_temp = """
    <div style="background-color:yellow;padding:10px">
    <p2 style="color:black;text-align:center;"> CROP YIELD PREDICTION FOR EAST AFRICA. </p2>
    
    </div>
    """
    
    """
      →   Agriculture is the African economy's backbone, providing employment and livelihoods for millions of people throughout the continent. According to the World Bank, agriculture contributes about 15% of Africa's G.D.P. and employs over 60% of the population in Sub-Saharan Africa (World Bank, 2022). However, smallholder farmers in Africa face various challenges that affect their productivity and crop yields. These challenges include unpredictable weather patterns, poor soil fertility, inadequate access to water, limited access to modern farming technologies and practices, and lack of food security in general (FAO, 2022). One of the most crucial aspects of Agriculture, Crop yield prediction, is essential for effective planning and decision-making in the agricultural sector, but accurate prediction remains a challenge. The traditional methods used in predicting crop yield are often inaccurate and inefficient. Therefore, there is a need to develop a more efficient and accurate technique for predicting crop yield in Africa. This is where machine learning comes in.
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    image = Image.open("cr2.jpg")   # Update the file path with your actual image file path
    st.image(image, caption='Crop Cultivation', use_column_width=True)

    """
       -> The use of machine learning technology in predicting crop yield has gained attention in recent years due to its potential to improve accuracy and efficiency. This project aims to develop a machine learning model that can accurately predict crop yield in Africa, thereby improving agricultural planning and resource allocation and ensuring food security.

Existing technologies such as remote sensing, satellite imagery, and weather forecasting models have been used to predict crop yields. However, these technologies have limitations, such as their inability to capture detailed information on soil moisture, crop phenology, and other crop growth factors. This is where machine learning can come in by providing more accurate and precise predictions of crop yields based on multiple variables and historical data.

The significance of this project lies in its potential to transform agriculture in Africa by enabling farmers to make data-driven decisions. Accurate yield predictions can help farmers optimize their resources, reduce waste, and increase profitability. Furthermore, improving crop yields can contribute to food security and poverty reduction in Africa, which are major United Nations Sustainable Development Goals(FAO, 2022).
By developing a machine learning model to predict crop yields in Africa, this project aims to contribute to achieving these goals.

    """
    
    image = Image.open("C4.jpg")   # Update the file path with your actual image file path
    st.image(image, caption='Crop Cultivation', use_column_width=True)

    """
List of Projects Specific Objectives 

→  Our list of objectives include:

→ To develop a machine learning model that can accurately predict crop yield in selected African countries, using relevant climate and soil data by the end of 2023. 

→ To achieve a minimum accuracy rate of 80% in predicting crop yield in the selected African countries. (If possible)

→ To identify the significant factors that affect crop yield in the selected African countries by conducting a comprehensive analysis of the data and make recommendations.

→ To provide insights and effective planning of agricultural activities and resources allocations.

→ (Optional) To develop an interactive dashboard or web-based application allowing farmers and policymakers to access crop yield predictions and other relevant information for the selected African countries by the end of 2023.

    """


if __name__=='__main__':
    main()
