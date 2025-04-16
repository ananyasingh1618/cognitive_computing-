from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text1 = "Artificial Intelligence is revolutionizing industries with automation and data-driven decisions."
text2 = "Blockchain ensures data security and decentralization across various systems."

tokens1 = set(text1.lower().split())
tokens2 = set(text2.lower().split())
jaccard = len(tokens1 & tokens2) / len(tokens1 | tokens2)

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform([text1, text2])
cos_sim = cosine_similarity(tfidf[0:1], tfidf[1:2])

print("Jaccard Similarity:", jaccard)
print("Cosine Similarity:", cos_sim[0][0])
