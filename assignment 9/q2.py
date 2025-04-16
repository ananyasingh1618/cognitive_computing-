import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
text = "Artificial intelligence (AI) refers to the ability of machines to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. It's a broad field encompassing various technologies, including machine learning, deep learning, and natural language processing. AI systems can analyze data, identify patterns, make predictions, and even generate creative content. "
tokens = word_tokenize(text.lower())
filtered = [w for w in tokens if w.isalpha() and w not in stopwords.words("english")]
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemma = WordNetLemmatizer()
porter_result = [porter.stem(w) for w in filtered]
lancaster_result = [lancaster.stem(w) for w in filtered]
lemmatized_result = [lemma.lemmatize(w) for w in filtered]
print("Porter:", porter_result)
print("Lancaster:", lancaster_result)
print("Lemmatized:", lemmatized_result)
