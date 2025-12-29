import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="centered"
)

# -------------------- LOAD MODEL --------------------
@st.cache_resource
def load_trained_model():
    return tf.keras.models.load_model(
        "brain_tumor_classifier_mobilenet.keras"
    )

model = load_trained_model()

# IMPORTANT: order must match training
CLASS_NAMES = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

# -------------------- UI --------------------
st.title("🧠 Brain Tumor Detection System")
st.write("Upload an **MRI Brain Image** to detect tumor type.")

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)

# -------------------- IMAGE PREPROCESSING --------------------
def preprocess_image(image):
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# -------------------- PREDICTION --------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)

    if st.button("🔍 Predict"):
        with st.spinner("Analyzing MRI..."):
            img = preprocess_image(image)
            prediction = model.predict(img)[0]

            class_index = np.argmax(prediction)
            confidence = prediction[class_index] * 100
            tumor_type = CLASS_NAMES[class_index]

        # -------------------- RESULT --------------------
        st.subheader("🧾 Prediction Result")

        if tumor_type == "No Tumor":
            st.success("✅ No Tumor Detected")
        else:
            st.error("⚠️ Tumor Detected")

        st.markdown(f"**Tumor Type:** {tumor_type}")
        st.markdown(f"**Confidence:** {confidence:.2f}%")

        st.progress(int(confidence))

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("⚕️ For educational and research purposes only.")
