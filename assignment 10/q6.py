from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.preprocessing.sequence import pad_sequences
import numpy as np
text = "Training data consists of input-output pairs, where the input, known as “features” or “predictors”, is matched with an output referred to as a “label” or “target.” These datasets contain various types of information – from images and text to numerical values and sensor readings."
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
total_words = len(tokenizer.word_index) + 1
input_sequence = []
for i in range(1, len(tokenizer.texts_to_sequences([text])[0])):
    n_gram_sequence = tokenizer.texts_to_sequences([text])[0][:i+1]
    input_sequence.append(n_gram_sequence)
max_sequence_length = max([len(x) for x in input_sequence])
input_sequence = pad_sequences(input_sequence, maxlen=max_sequence_length, padding='pre')
X, y = input_sequence[:, :-1], input_sequence[:, -1]
model = Sequential()
model.add(Embedding(total_words, 50, input_length=max_sequence_length-1))
model.add(LSTM(100))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

model.fit(X, y, epochs=100, verbose=1)

seed_word = "sun"
seed_sequence = tokenizer.texts_to_sequences([seed_word])
padded_seed_sequence = pad_sequences(seed_sequence, maxlen=max_sequence_length-1, padding='pre')

predicted_word = model.predict_classes(padded_seed_sequence, verbose=0)
print(tokenizer.index_word[predicted_word[0]])
