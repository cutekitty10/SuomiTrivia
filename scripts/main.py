def check_president():
    # Define the correct answer
    correct_answer = "alexander stubb"
    
    # Allow the user to try 3 times
    attempts = 3
    while attempts > 0:
        # Asking the user for the current president of Finland
        user_answer = input(f"Who is the current president of Finland? You have {attempts} attempts left: ").strip()

        # Checking the response
        if user_answer.lower() == correct_answer:
            print("Passed!")
            break
        else:
            print("Wrong answer!")
            attempts -= 1
    
    if attempts == 0:
        print("Sorry, you've used all your attempts!")

# Call the function if the script is run directly
if __name__ == "__main__":
    check_president()
