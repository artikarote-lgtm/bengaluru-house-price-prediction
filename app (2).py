from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load All Models
models = {
    "Random Forest": pickle.load(open("model.pkl", "rb")),
    "Linear Regression": pickle.load(open("linear_model.pkl", "rb")),
    "Decision Tree": pickle.load(open("decision_tree_model.pkl", "rb")),
    "XGBoost": pickle.load(open("xgboost_model.pkl", "rb"))
}

# Bengaluru locations
locations = [
    'Whitefield', 'Electronic City', 'Rajaji Nagar', 'Marathahalli', 'Indira Nagar',
    'Koramangala', 'Yelahanka', 'Bellandur', 'HSR Layout', 'Hebbal',
    'Kanakpura Road', 'Sarjapur Road', 'Bannerghatta Road', 'JP Nagar',
    'Uttarahalli', 'Kengeri', 'Chikkalasandra', 'Hoodi', 'KR Puram'
]

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Inputs
        model_name = request.form['model_choice']
        location = request.form['location']
        total_sqft = request.form['total_sqft']
        bhk = request.form['bhk']
        bath = request.form['bath']
        balcony = request.form['balcony']

        # Validation
        if not total_sqft.replace('.', '', 1).isdigit() or float(total_sqft) <= 0:
            return render_template('index.html', prediction="❌ Invalid Total Sqft", locations=locations)

        if not bhk.isdigit() or int(bhk) <= 0:
            return render_template('index.html', prediction="❌ Invalid BHK", locations=locations)

        if not bath.isdigit() or int(bath) <= 0:
            return render_template('index.html', prediction="❌ Invalid Bathrooms", locations=locations)

        if not balcony.isdigit() or int(balcony) < 0:
            return render_template('index.html', prediction="❌ Invalid Balcony Count", locations=locations)

        # Convert to numbers
        total_sqft = float(total_sqft)
        bhk = int(bhk)
        bath = int(bath)
        balcony = int(balcony)

        # Prepare DataFrame for model
        input_data = pd.DataFrame([{
            'location': location,
            'total_sqft': total_sqft,
            'bath': bath,
            'balcony': balcony,
            'bhk': bhk
        }])

        selected_model = models[model_name]
        predicted_price = selected_model.predict(input_data)[0]

        return render_template(
            'index.html',
            prediction=f"💰 {model_name} Prediction: {round(predicted_price, 2)} Lakhs",
            locations=locations
        )

    except Exception as e:
        return render_template('index.html', prediction=f"⚠️ Error: {str(e)}", locations=locations)

if __name__ == "__main__":
    app.run(debug=True)