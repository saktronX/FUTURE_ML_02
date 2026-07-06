import streamlit as st
import joblib

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Support Ticket Classification",
    page_icon="🎫",
    layout="centered"
)

# ----------------------------
# Load Models
# ----------------------------
try:
    ticket_model = joblib.load("models/classifier.pkl")
    priority_model = joblib.load("models/priority_classifier.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# ----------------------------
# Title
# ----------------------------
st.title("🎫 Support Ticket Classification")
st.write(
    "Predict the **Ticket Category** and **Priority Level** using Machine Learning."
)

# ----------------------------
# User Input
# ----------------------------
ticket = st.text_area(
    "Enter Support Ticket",
    height=200,
    placeholder="Example: My laptop battery keeps restarting after the latest software update."
)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict"):

    if ticket.strip() == "":
        st.warning("Please enter a support ticket.")
    else:
        try:
            ticket_vector = vectorizer.transform([ticket])

            ticket_prediction = ticket_model.predict(ticket_vector)[0]
            priority_prediction = priority_model.predict(ticket_vector)[0]

            st.success(f"🎫 **Ticket Category:** {ticket_prediction}")
            st.info(f"🚨 **Priority Level:** {priority_prediction}")

        except Exception as e:
            st.error(f"Prediction Error: {e}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Future Interns - Machine Learning Task 2 | Support Ticket Classification")