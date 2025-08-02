# List of questions, each as a dictionary with options and correct answer
quiz = [
    {
        "question": "What is the capital of India?",
        "options": {"a": "Delhi", "b": "Mumbai", "c": "Kolkata", "d": "Chennai"},
        "answer": "a"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {"a": "Earth", "b": "Venus", "c": "Mars", "d": "Jupiter"},
        "answer": "c"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": {"a": "Atlantic", "b": "Indian", "c": "Arctic", "d": "Pacific"},
        "answer": "d"
    }
]

# Score counter
score = 0

# Loop through each question
for index, q in enumerate(quiz, start=1):
    print(f"\nQ{index}: {q['question']}")
    for option, text in q["options"].items():
        print(f"  {option}) {text}")
    
    # Get user input
    user_answer = input("Your answer (a/b/c/d): ").lower()

    # Check if the answer is correct
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        correct_option = q["options"][q["answer"]]
        print(f"❌ Wrong! Correct answer: {q['answer']}) {correct_option}")

# Show final score
print(f"\n🏁 Quiz Complete! You scored {score} out of {len(quiz)}.")
