import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model
from time import sleep

# Load the saved model
model_path = 'model_improved.keras'
try:
    model = load_model(model_path)
except ValueError as e:
    st.error(f"Error loading model: {e}")

# Define the labels
labels = ['Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Pumpkin']

# Preprocess the image to match the model's input requirements
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to the correct dimensions
    image = np.array(image)
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def run():
    # Streamlit interface
    st.title('Vegetable Image Classification')
    st.write("Upload an image to classify it as Cabbage, Capsicum, Carrot, Cauliflower, or Pumpkin.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], help='Allowed file types: .jpg, .jpeg, .png')

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Make a prediction
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction, axis=1)[0]
        predicted_label = labels[predicted_class]
        probability = np.max(prediction) * 100

        # Add progression
        bar = st.progress(0)
        for percent_complete in range(101):
            sleep(0.005)
            bar.progress(percent_complete)
        st.success('Prediction Completed!')

        # Display the prediction and probability
        st.write(f"**Result: {predicted_label}**")
        st.write(f"**Confidence: {probability:.2f}%**")

        # Interpret the prediction
        if predicted_label == 'Cabbage':
            st.write("The image is classified as Cabbage. It has a dense-leaved head and is commonly used in various dishes.")
        elif predicted_label == 'Capsicum':
            st.write("The image is classified as Capsicum, known for its various colors and shapes, including bell peppers and chili peppers.")
        elif predicted_label == 'Carrot':
            st.write("The image is classified as Carrot, the familiar long, orange root vegetable.")
        elif predicted_label == 'Cauliflower':
            st.write("The image is classified as Cauliflower, depicted by its white, compact head surrounded by green leaves.")
        elif predicted_label == 'Pumpkin':
            st.write("The image is classified as Pumpkin, recognized by its round, orange fruit with a thick shell.")

if __name__ == "__main__":
    run()
