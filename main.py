print("Welcome to the Maths Quiz!")

score = 0

answer = input("What is 5 + 3? ")

if answer == "8":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is 10 - 4? ")

if answer == "6":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is 7 x 2? ")

if answer == "14":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("Quiz Complete!")
print("Your final score is:")
print(score)
