from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from textblob import TextBlob

healthbot = ChatBot(
    "HealthBot",
    read_only=True,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am not sure how to respond to that.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

trainer = ListTrainer(healthbot)
conversations = [
    'Hi',
    'Hello! I am HealthBot. How can I assist you today?',
    'Hello',
    'Hi! Do you have a health-related question?',
    'I have a headache',
    'You should rest, stay hydrated, and take a mild pain reliever if needed.',
    'What should I do if I have a fever?',
    'Drink plenty of fluids and rest. If the fever persists, please consult a doctor.',
    'I feel dizzy',
    'Sit down, breathe deeply, and drink water. If it continues, seek medical help.',
    'What should I eat for a cold?',
    'Warm fluids, soups, citrus fruits, and light meals help during a cold.',
    'How to stay healthy?',
    'Eat balanced meals, exercise regularly, stay hydrated, and get enough sleep.',
    'What should I do in case of a cut?',
    'Clean the wound with water, apply antiseptic, and cover it with a clean bandage.',
    'How much water should I drink daily?',
    'Generally, 2 to 3 liters per day is recommended, but it varies based on your activity.',
    'Thank you',
    'You’re welcome! Take care.',
    'Bye',
    'Goodbye! Stay healthy.'
]
trainer.train(conversations)

print("Ask something to HealthBot (type 'exit' to end):")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("HealthBot: Bye! Stay healthy.")
        break
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    if polarity < -0.3:
        prefix = "I'm sorry you're feeling that way. "
    elif polarity > 0.3:
        prefix = "That's great to hear! "
    else:
        prefix = ""
    response = healthbot.get_response(user_input)
    print(f"HealthBot: {prefix}{response}")
