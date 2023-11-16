"""
Assignment 1: This is a basic input and output file
September 10, 2023
Aaman Bhandari
"""

user_name = input("What is your name:\n")
valid_response = False
while not valid_response:
    python_knowledge = input("Do you know Python? (Sure/Yes/No/Not Sure):\n").strip().lower()

    if python_knowledge in ["yes", "no", "sure", "not sure"]:
        valid_response = True
    else:
        print("Please enter 'Yes' or 'No' as your response.")
print("Thanks for answering my questions, "+user_name)
if (python_knowledge) == "yes" or (python_knowledge) == "sure":
    print("Great to hear that you know Python!")
else:
    print("No worries! Python is a great language to learn.")