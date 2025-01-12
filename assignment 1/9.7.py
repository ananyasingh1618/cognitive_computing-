import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
random_card = random.choice(deck)
print(f"Random card: {random_card}")