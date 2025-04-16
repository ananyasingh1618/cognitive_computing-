from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

texts = [
    "The camera quality of this phone is outstanding and battery lasts long.",
    "This smartwatch has a sleek design and great performance.",
    "I am happy with the laptop speed and its lightweight body."
]

cv = CountVectorizer()
bow = cv.fit_transform(texts)
print("BoW Features:", cv.get_feature_names_out())
print("BoW Array:\n", bow.toarray())

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(texts)
features = tfidf.get_feature_names_out()
print("TF-IDF Features:", features)
print("TF-IDF Array:\n", tfidf_matrix.toarray())

for i, row in enumerate(tfidf_matrix.toarray()):
    top = row.argsort()[-3:][::-1]
    top_keywords = [features[j] for j in top]
    print("Top 3 Keywords for Text", i+1, ":", top_keywords)
