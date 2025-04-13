# Boston Housing Price Prediction Web App

This is a full-stack Machine Learning web application that predicts Boston house prices based on the average number of rooms using a regression model trained with Mini-Batch Gradient Descent and deployed using Flask and Render.

## Live App
- 🌐 [Render Web App](https://boston-housing-web-app.onrender.com)

## Model
- Hosted on Hugging Face: [Mini-Batch Regression Model](https://huggingface.co/Nabeeha-Shafiq/boston-housing-mini-batch-model)

## Training Dashboard (W&B)
- Run Log: [Batch-GD-L2 Training](https://wandb.ai/nabeeha529-fast-nuces/boston-housing-regression/runs/fa0pdkqb)
- Project: [boston-housing-regression](https://wandb.ai/nabeeha529-fast-nuces/boston-housing-regression)

## Project Structure
- `app.py`: Flask backend
- `templates/index.html`: UI form
- `requirements.txt`: Python dependencies
- `Procfile`: Render deployment config
- `inference.py`: inference script for local use

## How to Run Locally

1- Clone the repository / locally create exact same Project Structure:
git clone https://github.com/Nabeeha-Shafiq/boston-housing-web-app.git
cd boston-housing-web-app

2- Install dependencies:
pip install -r requirements.txt

3- Run the app:
python app.py

## How to Use the web application :

1- Enter average number of rooms in the web text box.
2- Enter PREDICT buttom to get house price prediction.
3- Model is loaded from Hugging Face at runtime.
