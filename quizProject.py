

# def main():
#     playGame()




# def generate_random_number():
#     import random
#     return(random.randint(1,100))


def player_guess():
    guess = (input("Guess a random number between 1-100: "))
    while(not guess.isdigit()):
        print("Enter a NUMBER between 1-100")
        return(player_guess())
    while(int(guess) > 100):
        print("Enter a NUMBER between 1-100")
        return(player_guess())
    return(int(guess))


def give_feedback(secret_number,  guess):
    if(guess > secret_number):
        print("Too high :( Guess again")
    elif(guess < secret_number):
        print("Too Low :( Guess again")
    elif(guess == secret_number):
        print ("You win :)")



def playGame():
    print("Guess a NUMBER 1-100, you have three tries. GOOD LUCK!!")
    

    secret_number = generate_random_number()
    guess = player_guess()
    

    
    give_feedback(secret_number,  guess)
    x = 0
    amount_of_tries = 1
    while(x < 2):
        if(secret_number == guess):
            x = 4
            amount_of_tries += 0
            y = 1

        elif(secret_number != guess):
            # guess = int(input("Guess a random number between 1-100: "))
            player_guess()
            give_feedback(secret_number,  guess)
            x += 1
            amount_of_tries += 1
            y = 2
    if(y == 1):
        print("It took you " + str(amount_of_tries) + " try.")
    elif(y == 2):
        print("You lost")
    print("The number is " + str(secret_number))
    
#     playAgian = input(("Do you want to play again? Yes - 1 or No - 2: "))
    
#     if(int(playAgian) == 1):
#         return(playGame())
#     else:
#         print("you suck")


# if __name__ == "__main__":
#     main()