from transformers import pipeline
import functools

@functools.cache
def load_classifier():
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    return classifier

def detect_emotions(schema):
    classifier = load_classifier()
    model_outputs = classifier([schema.text])
    return model_outputs[0]