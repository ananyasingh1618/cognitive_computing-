import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = "I enjoy exploring new technology. Innovations like AI and blockchain are changing the world. These tools simplify complex tasks and open new opportunities. Learning about tech trends is both fun and useful. The future of technology is fast and exciting."

clean = re.sub(r'[^\w\s]', '', text.lower())
alpha_words = re.findall(r'\b[a-zA-Z]+\b', clean)
filtered = [w for w in alpha_words if w not in stopwords.words("english")]
stemmed = [PorterStemmer().stem(w) for w in filtered]
lemmatized = [WordNetLemmatizer().lemmatize(w) for w in filtered]
print("Stemmed:", stemmed)
print("Lemmatized:", lemmatized)
