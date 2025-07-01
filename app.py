# from flask import Flask, render_template, request
# import pickle
# import numpy as np

# app = Flask(__name__)

# # Load model and scaler
# with open("cybersecurity_rf_model.pkl", "rb") as f:
#     model, scaler = pickle.load(f)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         features = [float(request.form[key]) for key in ['bytes_in', 'bytes_out', 'session_duration', 'avg_packet_size']]
#         features_scaled = scaler.transform([features])
#         prediction = model.predict(features_scaled)[0]
#         result = "Suspicious" if prediction == 1 else "Normal"
#     except Exception as e:
#         result = f"Error: {str(e)}"
#     return render_template("index.html", prediction=result)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
with open("cybersecurity_rf_model.pkl", "rb") as f:
    model, scaler = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_keys = ['bytes_in', 'bytes_out', 'session_duration', 'avg_packet_size']
        features = [float(request.form.get(k, 0)) for k in input_keys]
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0]
        result = "Suspicious" if prediction == 1 else "Normal"
    except Exception as e:
        result = f"Error: {str(e)}"
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

