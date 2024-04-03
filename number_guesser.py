import random

number = input("Enter a number:")

if number.isdigit():
    top = int(number)
    if top < 0:
        print("Enter above 0")
        quit()
else:
    print("Enter a number nxt time")

chances = 9
randomnumber = random.randint(0, 11)
while chances > 0:
    chances -= 1
    guess = input("guess a number?")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Type a number")
        continue
    if guess == randomnumber:
        print("Bingo!!")
        break
    elif guess > randomnumber:
        print("try again you are on a little higher end")
        continue
    elif guess < randomnumber:
        print(" try again you are on a little lower end")
        continue
    else:
        print("Wrong!")

print(" You guessed in ", guess, "guesses")
