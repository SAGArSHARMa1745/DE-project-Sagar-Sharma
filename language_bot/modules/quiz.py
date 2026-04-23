import random

def generate_quiz(words):
    return random.sample(words, min(5, len(words)))