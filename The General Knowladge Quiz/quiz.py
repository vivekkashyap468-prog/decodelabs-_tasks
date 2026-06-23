# The General Knowledge Quiz
# A fun terminal-based quiz game implementing Control Flow (If-Else logic) and Variables.

def run_quiz():
    print("=" * 50)
    print("         WELCOME TO THE GENERAL KNOWLEDGE QUIZ!         ")
    print("=" * 50)
    print("Test your knowledge! Answer the following 3 questions.\n")
    
    # Initialize score variable
    score = 0
    
    # Question 1
    print("Question 1: What is the capital of France?")
    print("A) London")
    print("B) Paris")
    print("C) Rome")
    answer1 = input("Your answer (A, B, or C): ").strip().upper()
    
    if answer1 == "B" or answer1 == "PARIS":
        print("[CORRECT] Excellent start.\n")
        score = score + 1
    else:
        print("[INCORRECT] The correct answer is B) Paris.\n")
        
    # Question 2
    print("Question 2: Which planet is known as the Red Planet?")
    print("A) Mars")
    print("B) Venus")
    print("C) Jupiter")
    answer2 = input("Your answer (A, B, or C): ").strip().upper()
    
    if answer2 == "A" or answer2 == "MARS":
        print("[CORRECT] Mars gets its red color from iron oxide.\n")
        score = score + 1
    else:
        print("[INCORRECT] The correct answer is A) Mars.\n")
        
    # Question 3
    print("Question 3: What is the largest ocean on Earth?")
    print("A) Atlantic Ocean")
    print("B) Pacific Ocean")
    print("C) Indian Ocean")
    answer3 = input("Your answer (A, B, or C): ").strip().upper()
    
    if answer3 == "B" or answer3 == "PACIFIC" or answer3 == "PACIFIC OCEAN":
        print("[CORRECT] The Pacific Ocean covers more than 30% of Earth's surface.\n")
        score = score + 1
    else:
        print("[INCORRECT] The correct answer is B) Pacific Ocean.\n")
        
    # Display final score
    print("=" * 50)
    print("                  QUIZ COMPLETED!                 ")
    print("=" * 50)
    print(f"Your final score is: {score} out of 3")
    
    # Custom feedback based on score (ASCII only for Windows compatibility)
    if score == 3:
        print("*** Perfect Score! You are a General Knowledge Master! ***")
    elif score == 2:
        print("Good job! You got most of them right.")
    elif score == 1:
        print("You got one correct. Keep learning!")
    else:
        print("Better luck next time! Time to hit the books.")
    print("=" * 50)

if __name__ == "__main__":
    run_quiz()
