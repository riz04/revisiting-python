print("..rock..")
print("..paper..")
print("..scissor..")

player1_choice = input("enter your choice player 1: ")

print(" ** No Cheating **\n " * 20)


player2_choice = input("enter your choice player 2: ")

if player1_choice == player2_choice:
    print ("Nobody wins")
elif player1_choice == "rock":
    if player2_choice == "paper":
        print("player2 wins")
    elif player2_choice == "scissor":
        print("player1 wins")
elif player1_choice == "paper":
    if player2_choice == "rock":
        print("player1 wins")
    elif player2_choice == "scissor":
        print("player2 wins")

elif player1_choice == "scissor":
    if player2_choice == "rock":
        print("player2 wins")
    elif player2_choice == "paper":
        print("player1 wins")
else:
    print("something went wrong")


