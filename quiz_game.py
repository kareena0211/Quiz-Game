
print("Welcome to my Quiz 😊")
playing = input( "Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct 🥳")
    score += 1
else:
    print("Incorrect 😢")

answer = input("Are you liking  this game? ")
if answer.lower() == "yes":
    print("Correct 🥳")
    score += 1
else:
    print("Incorrect 😢")

answer = input("Where is Taj Mahal? ")
if answer.lower() == "agra":
    print("Correct 🥳")
    score += 1
else:
    print("Incorrect 😢")

answer = input("Tell me the full form of RAM? ")
if answer.lower() == "random access memory":
    print("Correct 🥳")
    score += 1
else:
    print("Incorrect 😢")

answer = input("Tell me the English name of 'darvaja': ")
if answer.lower() == "door":
    print("Correct 🥳")
    score += 1
else:
    print("Incorrect 😢")

print("Your score for correct answers is =>", score)
print("You got " + str((score / 5) * 100) + "%")
