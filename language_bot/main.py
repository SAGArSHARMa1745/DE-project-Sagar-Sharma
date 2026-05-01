from modules.ingestion import load_words
from modules.quiz import generate_quiz
from modules.api import get_data
from modules.scoring import check
from modules.spaced import update_priority
from modules.db import save_bronze, save_silver, save_gold, get_stats

words = load_words("data/vocabulary.csv")

quiz = generate_quiz(words)

score = 0
wrong = 0

print("\n--- DAILY QUIZ ---")

for q in quiz:
    word = q['word']


    meaning, example, raw_json = get_data(word)

   
    save_bronze(word, raw_json)

    print(f"\nMeaning: {meaning}")
    ans = input("Guess the word: ")

    result = check(ans, word)

    if result:
        score += 1
        print("Correct")
    else:
        wrong += 1
        print(f"Wrong! Correct word: {word}")

    # update priority
    updated_word = update_priority(q, result)

    
    save_silver(word, meaning, example)


    save_gold(word, int(result), updated_word['priority'])

print("\nQuiz Finished")

print(f"\nCorrect Answers: {score}")
print(f"Wrong Answers: {wrong}")
print(f"Total Questions: {score + wrong}")

print("\n--- OVERALL TRACKER ---")
total_db, correct_db, wrong_db = get_stats()

print(f"Total Attempts (All Time): {total_db}")
print(f"Correct Answers: {correct_db}")
print(f"Wrong Answers: {wrong_db}")
