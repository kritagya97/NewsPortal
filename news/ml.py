import joblib
import re
from pathlib import Path
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Download NLTK data if missing
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")


# Load Machine Learning Model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "nb_model.joblib"

try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", e)


# NLP Setup
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))



# Text Preprocessing

def preprocess_text(text):

    try:
        # Convert to lowercase
        text = text.lower()

        # Remove numbers and special characters
        text = re.sub(r'[^a-zA-Z\s]', '', text)

        # Tokenize sentence into words
        words = word_tokenize(text)

        # Remove stopwords and perform lemmatization
        clean_words = []

        for word in words:
            if word not in stop_words:
                clean_words.append(lemmatizer.lemmatize(word))

        return " ".join(clean_words)

    except Exception as e:
        print("Error during preprocessing:", e)
        return ""


# Predict News Category
def predict_category(text):

    try:
        processed_text = preprocess_text(text)

        prediction = model.predict([processed_text])

        return prediction[0]

    except Exception as e:
        print("Prediction Error:", e)
        return None