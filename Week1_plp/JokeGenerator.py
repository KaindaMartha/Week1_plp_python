jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why did the Python programmer break up with the Java programmer? Because they had type issues.",
    "What do you call 8 hobbits? A hobbyte.",
    "Why did the developer go broke? Because he used up all his cache."
    "Why do Java developers wear glasses? Because they don't see sharp!",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    "Why do Python programmers prefer using snakes? Because they can handle exceptions!",
    "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
    "Why do programmers hate nature? It has too many bugs.",
    "Why did the coder get kicked off the plane? Because it was a no-fly zone for bugs!",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the web developer walk out of the meeting? Too many cookies and not enough cache!",
    "Why do programmers prefer using the terminal? Because they like to shell out!",
    "Why did the programmer go broke? Because he lost his domain in a bet!",
    "Why do programmers prefer using Python? Because it has a lot of 'byte'!",
    "Why did the developer stay calm during a crisis? Because he knew how to handle exceptions!"
]
def run_joke_generator():
    import random
    print("\nWelcome to the Joke Generator!")
    while True:
        joke = random.choice(jokes)
        print(f"\nHere's a joke for you: {joke}")
        cont = input("Do you want another joke? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thanks for using the Joke Generator! Goodbye!")
            break
# Run the joke generator
if __name__ == "__main__":
    run_joke_generator()
# --- IGNORE ---