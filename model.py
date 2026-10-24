"""
TF-IDF + PassiveAggressiveClassifier Pipeline for Misinformation Detection.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.pipeline import Pipeline

def build_detector_pipeline():
    return Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.7, ngram_range=(1, 2))),
        ('pac', PassiveAggressiveClassifier(max_iter=50, random_state=42))
    ])
