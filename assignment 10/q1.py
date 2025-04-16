import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
nltk.download('punkt')
nltk.download('stopwords')
text ="Artificial intelligence (AI) refers to the ability of machines to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. It's a broad field encompassing various technologies, including machine learning, deep learning, and natural language processing. AI systems can analyze data, identify patterns, make predictions, and even generate creative content"
clean = re.sub(r'[^\w\s]', '', text.lower())
words_split = clean.split()
words_tokenized = word_tokenize(clean)
sentences = sent_tokenize(text)
stop_words = set(stopwords.words("english"))
filtered = [w for w in words_tokenized if w not in stop_words]
freq = FreqDist(filtered)
print("Sentences:", sentences)
print("Split Words:", words_split)
print("Tokenized Words:", words_tokenized)
print("Filtered Words:", filtered)
print("Word Frequencies:", freq)
