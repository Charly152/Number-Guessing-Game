import random
n_try=1
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")
number_to_guess=random.randint(1,100)
chances=0
play=True

while play:
    diff=int(input("Choose difficulty level: \n1: Easy (10 chances) \n2: Medium (5 chances)\n3: Hard (3 chances) \nEnter your choice: "))
    if diff==1:
        print("\nGreat! You have selected the Easy difficulty level.\n")
        n_try=10
    elif diff==2:
        print("Great! You have selected the Medium difficulty level.\n")
        n_try=5
    elif diff==3:
        print("Great! You have selected the Hard difficulty level.\n")
        n_try=3

    print("Let's start the game!\n")

    for i in range(n_try):
        number_said=int(input("Enter your guess: "))
        if number_to_guess==number_said:
            print("Congratulations! You guessed the correct number in",i+1, "attempts.\n")
            break
        elif number_to_guess<=number_said:
            print("Incorrect! The number is less than", number_said,".\n")
            if i+1==n_try:
                print("You failed.")
        elif number_to_guess>=number_said:
            print("Incorrect! The number is greater than", number_said,".\n")
            if i+1==n_try:
                print("You failed.\n")
    play=bool(int(input("Do you want to play again: \n0: No \n1: Yes \nEnter your choice: \n")))  

        

