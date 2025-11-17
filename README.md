
🏠 Bengaluru House Price Prediction — Multi-Model ML Web App

This project is a web-based house price prediction system for Bengaluru, built using Machine Learning + Flask.
Users can enter property details and select the ML model (Linear Regression, Decision Tree, Random Forest, or XGBoost) to predict house prices in Lakhs.

🚀 Features

✔ Predicts house price based on user inputs
✔ Supports 4 ML models:

Linear Regression

Decision Tree

Random Forest

XGBoost

✔ Dynamic form — Shows only relevant fields based on House Type (Land / Apartment / Banglow)
✔ Clean Bootstrap UI
✔ Real-time predictions
✔ Fully trained .pkl models included
✔ Beginner-friendly code with comments

📂 Project Structure
project/
│── app.py
│── linear_model.pkl
│── decision_tree_model.pkl
│── random_forest_model.pkl
│── xgboost_model.pkl
│── Bengaluru_House_Custom.csv
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css

🧠 Machine Learning Models Used
1️⃣ Linear Regression

A simple model that finds a straight-line relationship between features and price.

2️⃣ Decision Tree

Splits data into branches to make predictions. Can overfit.

3️⃣ Random Forest

An ensemble of many decision trees → more accuracy, less overfitting.

4️⃣ XGBoost

A boosting algorithm that gives very high performance.

🧹 Dataset & Features Used

The dataset contains real estate data from Bengaluru with the following features:

✔ Used Features

Location

House Type

Age of Property

Total Sqft

BHK

Bathroom

Balcony

Metro Distance

Price (Target)

❌ Removed Features (too many missing/unhelpful)

Furnished

Parking

Floor

Society

🔧 How the System Works (Architecture)

1️⃣ User enters property details
2️⃣ Selects a machine learning model
3️⃣ Flask backend loads the respective .pkl model
4️⃣ Model predicts the price
5️⃣ Result shown instantly in the web UI

▶️ How to Run the Project
STEP 1 — Install required libraries
pip install flask pandas numpy scikit-learn xgboost

STEP 2 — Run the Flask App
python app.py

STEP 3 — Open in Browser
http://127.0.0.1:5000/

🎯 Model Comparison

All four models were trained and evaluated using:

R² Score

RMSE (Root Mean Square Error)

MAE (Mean Absolute Error)

Random Forest & XGBoost performed the best.

📌 Screenshots (Add your own)

You can paste screenshots of your UI here in GitHub later.

🙌 Conclusion

This project demonstrates how different machine learning algorithms can be used to predict real estate prices.
With a clean UI and multiple models to choose from, it serves as both a practical tool and a learning project for ML & Flask.

