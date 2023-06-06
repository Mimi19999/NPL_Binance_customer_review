# import data
import pandas as pd
df = pd.read_csv('/Users/mimi/binance_reviews.txt', sep="\n"*2, header=None)
print(df)
df = df.rename(columns={0: 'review'})
print(df)

# import library
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('wordnet')
nltk.download('omw-1.4')

# tokenization
df['word_review'] = df['review'].apply(lambda x: word_tokenize(x.lower()))
df['sent_review'] = df['review'].apply(lambda x: sent_tokenize(x.lower()))






