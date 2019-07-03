import random

random_number = random.randint(1,10)

guess = None
while guess != random_number:
    guess = int(input("pick a number from 1 to 10: "))
    if guess > random_number:
        print("Too High")
    elif guess < random_number:
        print("Too Low")
    else:
        print("You Won")
print(random_number)