import time
import threading
import sys
import os

def ask_question(question, correct_answers, total_time_event):
    """Asks a question and checks the answer. If wrong or time runs out, user loses the game."""
    answer_event = threading.Event()
    user_answer = None
    start_time = time.time()

    def get_input():
        nonlocal user_answer
        try:
            user_answer = input("Your answer: ").strip().lower()
            answer_event.set()
        except EOFError:
            pass  # Handle forced termination

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    while not answer_event.is_set():
        if total_time_event.is_set():
            return None  # Time's up, return None to signal game over
        time.sleep(0.1)
    
    elapsed_time = time.time() - start_time

    if user_answer in [ans.lower() for ans in correct_answers]:
        return elapsed_time  # Correct answer, return time taken
    else:
        return False  # Incorrect answer, return False

def quiz():
    """Finland Quiz: Answer all correctly or lose the game in 60 seconds!"""
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

    total_time_event = threading.Event()
    start_total_time = time.time()

    def total_timer():
        time.sleep(150)
        total_time_event.set()
        print("\nTime's up! You lost the game.")
        os._exit(1)  # Forcefully terminate the program

    timer_thread = threading.Thread(target=total_timer)
    timer_thread.daemon = True
    timer_thread.start()

    total_elapsed_time = 0

    for question, answers in questions:
        print(question)
        elapsed_time = ask_question(question, answers, total_time_event)
        
        if total_time_event.is_set():
            return  # Ensure clean exit when time runs out
        
        if elapsed_time is None:
            print("\nTime's up! You lost the game.")
            return
        elif elapsed_time is False:
            print("Wrong answer! You lost the game.")
            return
        else:
            total_elapsed_time += elapsed_time

    print(f"🎉 Congratulations! You passed the Finland quiz in {total_elapsed_time:.2f} seconds! 🇫🇮")


# Run the quiz
if __name__ == "__main__":
    quiz()