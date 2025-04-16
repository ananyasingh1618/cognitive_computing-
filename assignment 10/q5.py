from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reviews = [
    "I like this product, it's amazing!",
    "The product is terrible, do not buy it.",
    "It's okay, nothing special, just average."
]

analyzer = SentimentIntensityAnalyzer()
positive_reviews = []

for review in reviews:
    polarity = TextBlob(review).sentiment.polarity
    subjectivity = TextBlob(review).sentiment.subjectivity
    sentiment = "Neutral"
    if polarity > 0.1:
        sentiment = "Positive"
        positive_reviews.append(review)
    elif polarity < -0.1:
        sentiment = "Negative"
    print(f'Review: {review}\nSentiment: {sentiment}\nPolarity: {polarity}\nSubjectivity: {subjectivity}\n')

wordcloud = WordCloud().generate(" ".join(positive_reviews))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
