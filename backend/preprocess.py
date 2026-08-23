import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download only if not already installed
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

stop_words = set(stopwords.words("english"))


def preprocess(text):
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove numbers
    text = "".join(char for char in text if not char.isdigit())

    # Remove non-ASCII characters (emojis, etc.)
    text = "".join(char for char in text if char.isascii())

    # Tokenize
    words = word_tokenize(text)

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    return " ".join(words)