import random

score = 0

print("Select Difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty = input("Choose difficulty: ")

question_amount = int(input("How many questions would you like? "))

def ask_question():
    global score

    operators = ["+", "-", "*"]

    operator = random.choice(operators)

    if difficulty == "1":
        max_number = 10

    elif difficulty == "2":
        max_number = 50

    else:
        max_number = 100

    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)

    if operator == "+":
        correct_answer = num1 + num2

    elif operator == "-":
        correct_answer = num1 - num2

    else:
        correct_answer = num1 * num2

    while True:

        try:
            answer = int(input(f"What is {num1} {operator} {num2}? "))
            break

        except:
            print("Please enter a number.")

    if answer == correct_answer:
        print("Correct!")
        score += 1

    else:
        print("Wrong!")

play_again = "yes"

while play_again == "yes":

    score = 0

    print("Welcome to the Maths Quiz!")

    for i in range(question_amount):
        ask_question()

    print("Quiz Complete!")
    print("Your final score is:")
    print(score)

    play_again = input("Play again? (yes/no): ")
    