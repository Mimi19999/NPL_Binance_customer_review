# import data
import pandas as pd
df = pd.read_csv('/Users/mimi/binance_reviews.txt', sep="\n"*2, header=None)
print(df)
df = df.rename(columns={0: 'review'})


# import library
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re

# Download NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Data cleaning
# Remove special characters, symbols, numbers and combinations of letters and numbers
df['clean_text'] = df['review'].apply(lambda x: re.sub(r'[^A-Za-z\s]', '', x))
# Convert text to lowercase
df['clean_text'] = df['clean_text'].str.lower()
print(df['clean_text'].head(5))

# Check for unwanted patterns 
unwanted_patterns = ['@', '#', 'http', 'www', 'binance']
unwanted_data = df[df['clean_text'].str.contains('|'.join(unwanted_patterns))]
print(unwanted_data)

# Replace unwanted patterns with an empty string 
df['clean_text'] = df['clean_text'].replace('|'.join(unwanted_patterns), '', regex=True)
print(df['clean_text'].iloc[1988])

# tokenization
# df['word_review'] = df['review'].apply(lambda x: word_tokenize(x.lower()))

# removing stop words





