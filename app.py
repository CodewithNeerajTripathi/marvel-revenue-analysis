import streamlit as st
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Marvel Movie Revenue Predictor")
st.write("Enter values in millions")

opening = st.number_input("Opening Weekend Revenue (in millions $)", min_value=1.0, max_value=300.0, value=50.0)

north_america = st.number_input("Total North America Revenue (in millions $)", min_value=1.0, max_value=500.0, value=100.0)

if st.button("Predict Worldwide Revenue"):
    prediction = model.predict([[opening * 1_000_000, north_america * 1_000_000]])[0]
    profit = prediction / 1_000_000

    st.success(f"Predicted Worldwide Revenue: ${profit:.1f} Million")

    if profit < 300:
        st.warning("Revenue Category: Low")
    elif profit <= 800:
        st.info("Revenue Category: Medium")
    else:
        st.success("Revenue Category: High")