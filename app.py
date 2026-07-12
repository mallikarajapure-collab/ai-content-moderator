import streamlit as st
from transformers import pipeline

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Content Moderator",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI Content Moderator")
st.write("Analyze text and classify it as Safe or Toxic (Demo).")

# -----------------------------
# Load AI Model
# -----------------------------
@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

classifier = load_model()

# -----------------------------
# User Input
# -----------------------------
text = st.text_area(
    "Enter your text",
    placeholder="Type your message here..."
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Analyze"):

    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")

    else:
        result = classifier(text)[0]

        label = result["label"]
        confidence = result["score"] * 100

        st.subheader("Result")

        # Negative sentiment -> Toxic (Demo)
        if label == "NEGATIVE":
            st.error("🚫 Toxic Content Detected")
        else:
            st.success("✅ Safe Content")

        st.write(f"**Model Output:** {label}")
        st.write(f"**Confidence:** {confidence:.2f}%")

        st.progress(result["score"])