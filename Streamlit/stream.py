import os
import streamlit as st
import pickle
import numpy as np

# Get the absolute path to the pickle file
pickle_file_path = os.path.join(os.getcwd(), 'sample.pkl')

# Check if the file exists
if os.path.exists(pickle_file_path):
    with open(pickle_file_path, 'rb') as f:
        model = pickle.load(f)
else:
    st.error("Error: pickle file 'sample.pkl' not found.")
    st.stop()

def predict_marks(number_courses, time_study):
    input_data = np.array([[number_courses, time_study]]).astype(np.int16)
    pred = model.predict(input_data)
    return pred[0]

def main():
    st.title("Predict Marks")

    number_courses = st.number_input("Number of Courses")
    time_study = st.number_input("Time Study")

    if st.button("Predict"):
        prediction = predict_marks(number_courses, time_study)
        st.success(f"The predicted marks is: {float(prediction):.2f}")  # Convert prediction to float before formatting

if __name__ == "__main__":
    main()
