import random

print("..rock..")
print("..paper..")
print("..scissor..")

player_choice = input("enter your choice: ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissor"

print(f"computer plays {computer}")


if player_choice == computer:
    print ("Nobody wins")
elif player_choice == "rock":
    if computer == "paper":
        print("computer wins")
    else:
        print("player wins")
elif player_choice == "paper":
    if computer == "rock":
        print("player wins")
    else:
        print("computer wins")
elif player_choice == "scissor":
    if computer == "rock":
        print("computer wins")
    else:
        print("player wins")
else:
    print("Please enter a valid move")


