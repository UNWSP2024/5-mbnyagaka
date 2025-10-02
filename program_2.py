# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
import random

# Function to ask one quiz question
def ask_question():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)

    print("\n  ", num1)
    print("+ ", num2)
    print("------")

    answer = int(input("Your answer: "))
    correct = num1 + num2
    if answer == correct:
        print("Congratulations! That is correct.")
    else:
        print(f"Oops! The correct answer is {correct}.")
if __name__ == "__main__":
    print("Welcome to the Math Quiz!")
    ask_question()