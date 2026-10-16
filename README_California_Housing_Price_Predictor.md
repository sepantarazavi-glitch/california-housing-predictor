# California Housing Price Predictor

A personal machine learning project built to practice **regression, data analysis, model evaluation, and Streamlit application development** using the California Housing dataset.

The project explores how selected demographic and housing-related features can be used to predict the median house value of a California district. A Random Forest regression model is trained with Scikit-learn and then used in an interactive Streamlit application.

> **Project type:** Personal learning and practice project  
> **Focus:** Machine Learning, Data Analysis, Python, and Web Application Development

## Project Overview

This project follows a simple machine learning workflow:

1. Load the California Housing dataset.
2. Explore the data and relationships between variables.
3. Select relevant features for the prediction task.
4. Split the data into training and test sets.
5. Train a `RandomForestRegressor` model.
6. Evaluate the model using **R²** and **RMSE**.
7. Build an interactive Streamlit interface for making predictions.

## Features

- Exploratory data analysis with Pandas and Matplotlib/Seaborn.
- Feature correlation analysis.
- Random Forest regression using Scikit-learn.
- Train/test split for model evaluation.
- Model evaluation with R² and RMSE.
- Interactive Streamlit interface.
- User-controlled input parameters for generating a house-value prediction.

## Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Streamlit**
- **Pickle**

## Dataset

The project uses the **California Housing dataset** provided through Scikit-learn's `fetch_california_housing()` function.

The model uses the following features:

- `MedInc` — Median income
- `HouseAge` — Median house age
- `AveRooms` — Average number of rooms
- `AveBedrms` — Average number of bedrooms

The target variable is:

- `MedHouseVal` — Median house value

## Machine Learning Model

The main model used in the project is a **Random Forest Regressor**.

The notebook includes:

- an 80/20 train-test split,
- model training,
- predictions on the test set,
- R² evaluation,
- RMSE evaluation.

The notebook and Streamlit application use slightly different Random Forest configurations because the application was created separately as an interactive implementation.

## Streamlit Application

The project includes a Streamlit application where users can enter housing parameters using interactive sliders.

The application uses:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms

After clicking **Predict Price**, the trained model returns an estimated house value.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/sepantarazavi-glitch/california-housing-price-predictor.git
cd california-housing-price-predictor
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

## Project Structure

```text
california-housing-price-predictor/
│
├── app.py
├── analysis.ipynb
├── requirements.txt
├── README.md
└── house_price_model.pkl
```

The exact file structure may vary depending on the version of the project.

## What I Practiced

Through this project, I practiced:

- Working with a real-world dataset.
- Exploring and visualizing data.
- Selecting features for a regression problem.
- Training a machine learning model with Scikit-learn.
- Evaluating regression models.
- Working with Python data science libraries.
- Building a simple interactive web application with Streamlit.
- Connecting a machine learning model to a user interface.

## Possible Improvements

Some possible next steps for this project include:

- Comparing Random Forest with other regression algorithms.
- Performing hyperparameter tuning.
- Adding more features to the model.
- Improving the Streamlit interface.
- Separating data preparation, model training, and application code.
- Saving and loading a finalized trained model instead of training it when the application starts.
- Adding additional evaluation visualizations.

## Disclaimer

This project was created as a **personal learning and practice project** to develop practical skills in Python, data analysis, machine learning, and application development. The predictions are intended for demonstration and learning purposes and should not be used as professional real-estate valuations.
