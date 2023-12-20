from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import streamlit as st


model = AutoModelForImageClassification.from_pretrained('facebook/dinov2-small-imagenet1k-1-layer')
processor = AutoImageProcessor.from_pretrained('facebook/dinov2-small-imagenet1k-1-layer')


st.title('Классификация изображений на основе модели facebook/dinov2-small')

def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания', type=['png', 'jpg'])
    if uploaded_file is not None:
        image_data = Image.open(uploaded_file)
        st.image(image_data)
        return(image_data)
    else:
        return None

img = load_image()

result = st.button('Распознать изображение')

if result:
    inputs = processor(images=img, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    st.write('**Результаты распознавания:**', model.config.id2label[predicted_class_idx])