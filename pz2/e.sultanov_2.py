from transformers import MobileViTFeatureExtractor, MobileViTForImageClassification
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Image Classification", page_icon=":shark:")

st.title('Welcome to the Image Classification website')

st.markdown('## Choose an image you want to classificate')

feature_extractor = MobileViTFeatureExtractor.from_pretrained("apple/mobilevit-small")
model = MobileViTForImageClassification.from_pretrained("apple/mobilevit-small")

img = st.file_uploader("Please, choose your image", type=['png', 'jpg'])
if img is not None:
    st.image(img)
    inputs = feature_extractor(images=Image.open(img), return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    # model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()
    res = model.config.id2label[0]  

st.sidebar.write("# Choose an image first")
btn = st.sidebar.button("Recognize")
if btn and img:
    st.sidebar.write("# Predicted class:", res)
    st.balloons()
elif btn:
    st.sidebar.write("# Choose an image")
