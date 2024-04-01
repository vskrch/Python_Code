chances = 3

name = input("Enter your name to start the quiz:")

print("Welcome {0} to the Computer Quiz! ".format(name))
scoreBoard = 0
while chances > 0:
    answer = input("what is CPU")
    if answer.lower() == "central processing unit":
        scoreBoard+=1
    else:
        print("Incorrect")
        chances -=1

    answer = input("What is Gpu")
    if answer.lower() == "Graphics processing unit":
        scoreBoard+=1

    else:
        print("incorrect")
        chances -=1
    answer = input("What is int")
    if answer.lower() == "integer":
        scoreBoard+=1
    else:
        print("Incorrect")
        chances -= 1

if chances == 0:
    print("You Lost!")
else:
    print("Hey {0} your score is :"+str(((scoreBoard/3)*100))+"%. ".format(name))