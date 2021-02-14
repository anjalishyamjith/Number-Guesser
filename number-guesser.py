import random

below = "Your number is BELOW the actual number. Try again."
above = "Your number is ABOVE the actual number. Try again."
win = "Congrats! You guessed it right!!"
lose = "Bring some more luck next time."
sep = "-" * 50

choice = input('''Select Game Level:
------------------
1. Beginner
    Turns: Infinite
    Range: 1 - 50\n
2. Intermediate
    Turns: 10
    Range: 1 - 100\n
3. Advance
    Turns: 5
    Range: 1 - 200\n
--> ''')

if choice == "Beginner" or choice == "beginner" or choice == "1":
    pc = random.randint(1, 50)

elif choice == "Intermediate" or choice == "Intermediate" or choice == "2":
    pc = random.randint(1, 100)
    turns = 10

elif choice == "Advance" or choice == "advance" or choice == "3":
    pc = random.randint(1, 200)
    turns = 5

else:
    print("Invalid Input try again...")

game = True

while game:

    while choice == "Beginner" or choice == "beginner" or choice == "1" and game:
        user = int(input("Enter number: "))
        print("\n", sep)

        if user < pc:
            print(below)
            print("\n", sep)

        elif user > pc:
            print(above)
            print("\n", sep)

        else:
            print(win)
            game = False

    while ((choice == "Intermediate" or choice == "intermediate" or choice == "2") or
           (choice == "Advance" or choice == "advance" or choice == "3")) \
            and turns > 0 \
            and game:
        user = int(input("Enter number: "))
        print("\n", sep)

        if user < pc:
            print(below)
            turns = turns - 1
            print(f"You have {turns} turns left.")
            print("\n", sep)

        elif user > pc:
            print(above)
            turns = turns - 1
            print(f"You have {turns} turns left.")
            print("\n", sep)

        else:
            print(win)
            turns = 0
            game = False

        if turns == 0:
            print(lose)
            game = False
