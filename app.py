import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

@st.cache_resource
def get_trained_model():
    housing = fetch_california_housing(as_frame=True)
    X = housing.data[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms']]
    y = housing.target
    
    model = RandomForestRegressor(n_estimators=50, max_depth=12, random_state=42)
    model.fit(X, y)
    return model

model = get_trained_model()

st.title("California Housing Price Predictor")
st.write("This web application predicts median house values based on geographical and demographic features using a machine learning model.")

st.header("Property Parameters")
med_inc = st.slider("Median Income", 0.5, 15.0, 3.0)
house_age = st.slider("House Age (Years)", 1, 50, 20)
ave_rooms = st.slider("Average Rooms", 1.0, 10.0, 5.0)
ave_bedrms = st.slider("Average Bedrooms", 1.0, 4.0, 1.0)

if st.button("Predict Price"):
    input_data = pd.DataFrame([[med_inc, house_age, ave_rooms, ave_bedrms]], 
                              columns=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms'])
    prediction = model.predict(input_data)[0]
    
    st.success(f"Estimated House Price: ${prediction * 100000:,.2f}")
