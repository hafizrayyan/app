import streamlit as st
import pickle 

with open("Student_performance_prediction.pkl", mode = "rb") as f :
    model = pickle.load(f)


st.title("Student Performance Prediction")
hours_studied = st.number_input("Hours Studied ",value = 0)
previous_scores = st.number_input("Previous Score ",value = 0)

status = st.button("Predict")

if status :
    prediction = model.predict([[hours_studied,previous_scores]])
    print(prediction)

    st.success(f"Predicted Performance Index: {prediction[0]:.2f}")


