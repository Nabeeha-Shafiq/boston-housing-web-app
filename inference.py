from huggingface_hub import hf_hub_download
import joblib

# === Step 1: Download model and scaler from Hugging Face ===
model_path = hf_hub_download(repo_id="Nabeeha-Shafiq/boston-housing-mini-batch-model", filename="mini_batch_model.joblib")
scaler_path = hf_hub_download(repo_id="Nabeeha-Shafiq/boston-housing-mini-batch-model", filename="scaler.joblib")

# === Step 2: Load model and scaler ===
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# === Step 3: Accept user input and predict ===
while True:
    try:
        rm = float(input("Enter average number of rooms (RM): "))
        X_new = scaler.transform([[rm]])
        prediction = model.predict(X_new)
        print(f"🏠 Predicted house price: ${prediction[0]*1000:.2f}")
    except KeyboardInterrupt:
        print("\n🛑 Exiting...")
        break
    except:
        print("❌ Invalid input. Please enter a number.")
