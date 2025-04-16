import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = "Artificial intelligence (AI) refers to the ability of machines to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. It's a broad field encompassing various technologies, including machine learning, deep learning, and natural language processing. AI systems can analyze data, identify patterns, make predictions, and even generate creative content."

cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
words = word_tokenize(cleaned_text)
sentences = sent_tokenize(text)
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word not in stop_words]
word_freq = nltk.FreqDist(filtered_words)

print("\nText Analysis Results:")
print("Sentences:", sentences)
print("\nWords:", words)
print("\nFiltered Words:", filtered_words)
print("\nWord Frequencies:", dict(word_freq))

porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

porter_stems = [porter.stem(word) for word in filtered_words]
lancaster_stems = [lancaster.stem(word) for word in filtered_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print("\nWord Forms:")
print("Porter:", porter_stems)
print("Lancaster:", lancaster_stems)
print("Lemma:", lemmatized_words)

print("\nPattern Analysis:")
print("Words >5 letters:", re.findall(r'\b\w{6,}\b', text))
print("Numbers:", re.findall(r'\b\d+\b', text))
print("Capitalized:", re.findall(r'\b[A-Z][a-z]*\b', text))

alpha_words = re.findall(r'\b[a-zA-Z]+\b', text)
vowel_words = [word for word in alpha_words if word[0].lower() in 'aeiou']
print("\nWord Categories:")
print("Only Alphabets:", alpha_words)
print("Starts with Vowel:", vowel_words)

def custom_tokenizer(text):
    text = re.sub(r'[^\w\s\'\-\.]', '', text)
    tokens = re.findall(r'\d+\.\d+|\w+(?:-\w+)*|\'\w+|\w+', text)
    return tokens

print("\nCustom Analysis:")
print("Custom Tokens:", custom_tokenizer(text))

text_with_substitutions = text
text_with_substitutions = re.sub(r'\S+@\S+', '<EMAIL>', text_with_substitutions)
text_with_substitutions = re.sub(r'https?://\S+|www\.\S+', '<URL>', text_with_substitutions)
text_with_substitutions = re.sub(r'(\+91[\s-]?\d{10})|(\d{3}[-\s]\d{3}[-\s]\d{4})', '<PHONE>', text_with_substitutions)
print("\nText Substitutions:")
print("Substituted Text:", text_with_substitutions)