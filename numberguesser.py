import random

def main():
    
    print("Welcome to the number guessing game!")
    print("Let's see what you've got! Try to guess a number from 1 to 100. You have 3 tries")
    generate_random_number = random.randint(1, 100)
    
    # maxattempts = 3
    # for playerguess in range(1,maxattempts + 1):
    #     playerguess = int(input("please enter an integer from 1 to 100:"))
    #     if playerguess > generate_random_number and playerguess < 101:
    #         print("That guess was too high")
    #     elif playerguess < generate_random_number and playerguess > 0:
    #         print("That guess was too low")
    #     elif playerguess == generate_random_number:
    #         print("Thats it, You Win!")
    #     elif  playerguess > 100:
    #         print("That Guess Doesn't Fit The Criteria, you have waisted a guess.")
    #     elif playerguess < 1:
    #         print("That Guess Doesn't Fit The Criteria, you have waisted a guess.")
    #     elif playerguess.isnotdigit:
    #          print("That Guess Doesn't Fit The Criteria, you have waisted a guess.")
    # else:
    #     print("Sorry you have run out of tries.")
    #     print("The correct number was",generate_random_number)
        
    playAgain = input(("Do you want to play again? Yes 1 or No anything else: "))
    
    if(int(playAgain) == 1):
        return(main())
    else:
        print("you suck")



if __name__ == "__main__":
    main()


