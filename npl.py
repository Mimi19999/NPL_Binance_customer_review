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

# tokenization
df['tokenized_clean_text'] = df['clean_text'].apply(lambda x: word_tokenize(x))

# removing stop words
stop_words = set(stopwords.words('english'))
df['filtered_reviews'] = df['tokenized_clean_text'].apply(lambda x: [word for word in x if word not in stop_words])

# Lemmatization
lemmatizer = WordNetLemmatizer()
df['lemmatized_reviews'] = df['filtered_reviews'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
print(df['lemmatized_reviews'].head(5))

# Join the preprocessed reviews back into text
df['preprocessed_reviews'] = df['lemmatized_reviews'].apply(lambda x: ' '.join(x))
print(df['preprocessed_reviews'].head(5))

# Vectorization
from sklearn.feature_extraction.text import CountVectorizer
vectorize = CountVectorizer()
X = vectorize.fit_transform(df['preprocessed_reviews'])

# Top Modeling with LDA
from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=10, random_state=42, learning_method='online')
lda.fit(X)
print(lda.components_)

# Get the most important words for each topic
feature_names = vectorize.get_feature_names_out()
print(feature_names)
topics = {}
for topic_idx, topic in enumerate(lda.components_):
    print(topic_idx, topic)
    top_words = [feature_names[i] for i in topic.argsort()[:-6:-1]]
    print(top_words)
    topics[f"Topic {topic_idx+1}"] = top_words
print(topics)

# Topic classification for each review
df['topic'] = lda.transform(X).argmax(axis=1) + 1

# Visualisation
import seaborn as sns
import matplotlib.pyplot as plt
topic_count = df['topic'].value_counts().sort_index()
print(topic_count)
plt.figure(figsize=(10, 6))
sns.barplot(x=topic_count.index, y=topic_count.values)
plt.xlabel('Topic')
plt.ylabel('Count')
plt.title('Topic Distribution')
plt.show()






