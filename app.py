from flask import Flask, request, render_template
from huggingface_hub import hf_hub_download
import joblib

app = Flask(__name__)

# Download model and scaler from Hugging Face
model_path = hf_hub_download(repo_id="Nabeeha-Shafiq/boston-housing-mini-batch-model", filename="mini_batch_model.joblib")
scaler_path = hf_hub_download(repo_id="Nabeeha-Shafiq/boston-housing-mini-batch-model", filename="scaler.joblib")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        try:
            rm = float(request.form["rooms"])
            rm_scaled = scaler.transform([[rm]])
            pred = model.predict(rm_scaled)
            prediction = f"${pred[0]*1000:.2f}"
        except:
            prediction = "Invalid input. Please enter a number."

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
