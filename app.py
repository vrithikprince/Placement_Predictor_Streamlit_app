import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("🎓 Placement Prediction App")

# Input fields
iq = st.number_input("Enter IQ (e.g. 100 - 160)", min_value=0.0, max_value=200.0, step=1.0)
cgpa = st.number_input("Enter CGPA (e.g. 6.0 - 10.0)", min_value=0.0, max_value=10.0, step=0.1)

# Button to trigger prediction
if st.button("Predict Placement"):
    input_data = np.array([[iq, cgpa]])
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1 or prediction == 'Yes':
        st.success("🎉 Candidate is likely to be Placed ✅")
    else:
        st.error("❌ Candidate is unlikely to be Placed")
