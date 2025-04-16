import re
text = "Artificial intelligence (AI) refers to the ability of machines to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. It's a broad field encompassing various technologies, including machine learning, deep learning, and natural language processing. AI systems can analyze data, identify patterns, make predictions, and even generate creative content"
def custom_tokenizer(t):
    t = re.sub(r'[^\w\s\'\-\.]', '', t)
    tokens = re.findall(r'\d+\.\d+|\w+(?:-\w+)*|\'\w+|\w+', t)
    return tokens
tokens = custom_tokenizer(text)
text_cleaned = re.sub(r'\S+@\S+', '<EMAIL>', text)
text_cleaned = re.sub(r'https?://\S+|www\.\S+', '<URL>', text_cleaned)
text_cleaned = re.sub(r'(\+91[\s-]?\d{10})|(\d{3}[-\s]\d{3}[-\s]\d{4})', '<PHONE>', text_cleaned)
print("Custom Tokens:", tokens)
print("Cleaned Text:", text_cleaned)
