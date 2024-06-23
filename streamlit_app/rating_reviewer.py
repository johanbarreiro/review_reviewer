import pandas as pd
from transformers import pipeline

# Define the zero-shot classification pipeline using DeBERTa
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")

# Define the labels for classification
labels = ["very bad review", "bad review", "average review", "good review", "very good review"]

# Function to classify a single piece of text
def classify_text(text):
    result = classifier(text, labels)
    return result['labels'][0]  # The label with the highest score

# Function to convert labels to ratings
def convert_label_to_rating(label):
    label_to_rating = {
        "very bad review": 1,
        "bad review": 2,
        "average review": 3,
        "good review": 4,
        "very good review": 5
    }
    return label_to_rating[label]
