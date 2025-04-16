import re
text = "Artificial intelligence (AI) refers to the ability of machines to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. It's a broad field encompassing various technologies, including machine learning, deep learning, and natural language processing. AI systems can analyze data, identify patterns, make predictions, and even generate creative content. "
words_long = re.findall(r'\b\w{6,}\b', text)
numbers = re.findall(r'\b\d+\b', text)
capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)
alpha_only = re.findall(r'\b[a-zA-Z]+\b', text)
vowel_start = [w for w in alpha_only if w[0].lower() in 'aeiou']
print("Words > 5 letters:", words_long)
print("Numbers:", numbers)
print("Capitalized Words:", capital_words)
print("Alphabet Words:", alpha_only)
print("Words Starting with Vowel:", vowel_start)
