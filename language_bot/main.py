from modules.ingestion import load_words
from modules.quiz import generate_quiz
from modules.api import get_data
from modules.scoring import check
from modules.spaced import update_priority
from modules.db import save_result, get_stats

# load words from CSV
words = load_words("data/vocabulary.csv")

# generate quiz
quiz = generate_quiz(words)

score = 0
wrong = 0

print("\n--- DAILY QUIZ ---")

for q in quiz:
    word = q['word']
    
    meaning, example = get_data(word)
    
    print(f"\nMeaning: {meaning}")
    ans = input("Guess the word: ")
    
    result = check(ans, word)
    
    if result:
        score += 1
        print("Correct ✅")
    else:
        wrong += 1
        print(f"Wrong ❌ | Correct word: {word}")
    
    # update spaced repetition
    update_priority(q, result)
    
    # save result in database
    save_result(word, int(result))

print("\nQuiz Finished 🎯")

# current quiz result
print(f"\nCorrect Answers: {score}")
print(f"Wrong Answers: {wrong}")
print(f"Total Questions: {score + wrong}")

# overall tracking from database
print("\n--- OVERALL TRACKER ---")

total_db, correct_db, wrong_db = get_stats()

print(f"Total Attempts (All Time): {total_db}")
print(f"Correct Answers: {correct_db}")
print(f"Wrong Answers: {wrong_db}")