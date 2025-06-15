# Placement_Predictor_Streamlit_app
This project is a simple and interactive machine learning web application built using Streamlit that predicts whether a student will be placed or not based on their IQ and CGPA. The model used for prediction is trained and saved as model.pkl

🚀 Features
🧠 Uses a trained ML model (model.pkl) for binary classification (Placed: Yes/No)
📊 Takes user input for IQ and CGPA
⚡ Instant prediction on button click
💡 Simple and clean UI using Streamlit

🛠️ Tech Stack
Python 🐍
Streamlit 🌐
Scikit-learn / Pickle 📦 (for model serialization)

📁 Folder Structure
placement_predictor/
├── model.pkl          # Trained machine learning model
├── app.py             # Streamlit frontend application

📌 How to Run
pip install streamlit
streamlit run app.py
Make sure model.pkl is present in the same directory.
