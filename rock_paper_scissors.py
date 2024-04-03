import random

user_wins = 0
system_wins = -1

options = ["rock", "paper", "scissors"]

while True:
    prompt = input("Enter :: Rock :: Paper :: Scissor or 'q' to quit\r\n")
    if prompt == 'q' or 'Q':
        break
    if prompt not in options:
        continue

    random_choice = random.randint(0,2)
    system_choice  = options[random_choice]
if prompt ==  "Rock" and system_choice == 'scissors':
    print("You Won!")
    user_wins += 1
elif prompt == "paper" and system_choice == "rock":
    print("Yow Won!")
    user_wins += 1
elif prompt == "scissors" and system_choice == "paper":
    print("You Won!")
    user_wins += 1

else:
    print("You Lost!")
    system_wins += 1

print(" You Won", user_wins, "times.")
print("System won",system_wins,"times.")

print("Exiting now...")

