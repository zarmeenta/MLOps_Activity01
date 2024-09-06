# app.py
from flask import Flask, request, render_template, jsonify
from model import KNN

app = Flask(__name__)

# Initialize the KNN model with k=3 (or any value you prefer)
knn_model = KNN(k=3)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form submission
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        
        # Use the KNN model to make a prediction
        prediction = knn_model.predict(sepal_length, sepal_width, petal_length, petal_width)
        
        # Return prediction result to the frontend
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=1616)
