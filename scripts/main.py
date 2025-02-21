import time
import threading
import sys
import os

def ask_question(question, correct_answers, attempts_left):
    """Asks a question and checks the answer. If wrong, user loses an attempt but stays on the same question. If time runs out, all attempts are lost."""
    while True:
        user_answer = None
        answer_event = threading.Event()

        def get_input():
            nonlocal user_answer
            user_answer = input("Your answer: ").strip().lower()
            answer_event.set()
        
        def display_timer():
            print(f"[20 seconds to answer] Attempts left: {attempts_left}")

        display_timer()
        thread = threading.Thread(target=get_input)
        thread.daemon = True
        thread.start()

        thread.join(timeout=20)  # Wait for answer, timeout after 20 seconds

        if not answer_event.is_set():
            print("\nTime's up! You lost all attempts. Game over.")
            sys.exit(1)  # Exit the game if time runs out
        
        if user_answer in [ans.lower() for ans in correct_answers]:
            return attempts_left  # Correct answer, return remaining attempts
        else:
            attempts_left -= 1
            if attempts_left == 0:
                print("Wrong answer! No attempts left. Game over.")
                sys.exit(1)
            print(f"Wrong answer! Attempts left: {attempts_left}")
            # Continue the loop with the reduced attempt count

def save_time_to_leaderboard(time_taken):
    """Saves the quiz completion time to a leaderboard file and sorts it."""
    leaderboard_file = "leaderboard.txt"
    times = []

    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            times = [float(line.strip()) for line in file.readlines()]
    
    times.append(time_taken)
    times.sort()

    with open(leaderboard_file, "w") as file:
        for t in times:
            file.write(f"{t}\n")

    print("\n🏆 Leaderboard: Fastest Completion Times 🏆")
    for i, t in enumerate(times, 1):
        print(f"{i}. {t:.2f} seconds")

def quiz():
    """Finland Quiz: Answer all correctly or lose the game!"""
    questions = [
        ("Who is the current president of Finland?", ["Alexander Stubb", "Alexander", "Stubb"]),
        ("What is the current capital city of Finland?", ["Helsinki"]),
        ("What is Finland’s official currency?", ["Euro"]),
        ("Name one country that borders Finland:", ["Russia", "Sweden", "Norway"]),
        ("What is Finland's national animal?", ["Brown bear", "Bear"]),
        ("What is the official language of Finland?", ["Finnish", "Swedish"]),
        ("What is Finland’s largest lake?", ["Lake Saimaa", "Saimaa"]),
        ("Which Finnish company is famous for mobile phones?", ["Nokia"]),
        ("What is the name of Finland’s national anthem?", ["Maamme", "Maamme Laulu"]),
        ("What is Finland’s independence day? (format: DD Month)", ["6 December", "6 12"]),
        ("What is the northernmost region of Finland called?", ["Lapland"]),
        ("What is the Finnish word for ‘hello’?", ["Moi", "Hei"]),
        ("What colors are in the Finnish flag?", ["White and blue", "Blue and white", "White blue", "Blue white", "White, blue", "Blue, white"]),
        ("When did Finland get independence?", ["1917"]),
        ("What was Finland's first capital city?", ["Turku"]),
        ("Which Finnish composer wrote ‘Finlandia’?", ["Jean Sibelius", "Sibelius", "Jean"]),
        ("What is the most popular sport in Finland?", ["Ice hockey", "Icehockey"]),
        ("What type of sauna is traditional in Finland?", ["Smoke sauna", "Smoke"]),
        ("Is Finland a Nordic country?", ["Yes", "Yeah"]),
        ("Where does the Finnish Santa Claus live?", ["Rovaniemi", "Tunturi", "Pohjois tunturi"]),
    ]

    attempts = 3
    start_time = time.time()
    for question, answers in questions:
        print("\n" + question)
        attempts = ask_question(question, answers, attempts)
    
    total_time = time.time() - start_time
    print(f"\n🎉 Congratulations! You passed the Finland quiz in {total_time:.2f} seconds! 🇫🇮")
    save_time_to_leaderboard(total_time)

# Run the quiz
if __name__ == "__main__":
    quiz()
