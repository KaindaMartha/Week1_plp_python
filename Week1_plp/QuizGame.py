import time

# Define questions and answers
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["a) def", "b) func", "c) define", "d) lambda"],
        "answer": "a"
    },
    {
        "question": "What is the highest-grossing film of all time (as of 2025)?",
        "options": ["a) Titanic", "b) Avatar", "c) Avengers: Endgame", "d) Star Wars: The Force Awakens"],
        "answer": "b"
    },
    {
        "question": "Which data structure uses key-value pairs in Python?",
        "options": ["a) list", "b) tuple", "c) set", "d) dictionary"],
        "answer": "d"
    },
    {
        "question": "In the movie 'The Matrix', what color is the pill Neo takes?",
        "options": ["a) Blue", "b) Yellow", "c) Red", "d) Green"],
        "answer": "c"
    },
    {
        "question": "What will `print(type([]))` output in Python?",
        "options": ["a) <class 'list'>", "b) <type 'list'>", "c) list", "d) <list>"],
        "answer": "a"
    }
]

def run_quiz():
    print("\nWelcome to the Python & Fun Quiz!")
    score = 0

    # Loop through each question
    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (a/b/c/d): ").lower()

        # Check answer
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']})")

        time.sleep(1)

    # Display final score
    print("\nQuiz Complete!")
    print(f"Your Score: {score} out of {len(questions)}")
    if score == len(questions):
        print("Perfect score! You're a quiz master!")
    elif score >= 3:
        print("Good job! Keep practicing.")
    else:
        print("Better luck next time!")

    # Ask to play again
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again == "yes":
        run_quiz()
    else:
        print("Thanks for playing! See you next time.")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
