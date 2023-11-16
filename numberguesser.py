import random

def main():
    
    print("Welcome to the number guessing game!")
    print("Let's see what you've got! Try to guess a number from 1 to 100. You have 3 tries")
    correctnumber = random.randint(1, 100)
    
    maxattempts = 3
    for playerguess in range(1,maxattempts + 1):
        playerguess = int(input("please enter an integer from 1 to 100:"))
        if playerguess > correctnumber and playerguess < 101:
            print("That guess was too high")
        elif playerguess < correctnumber and playerguess > 0:
            print("That guess was too low")
        elif playerguess == correctnumber:
            print("Thats it, You Win!")
        elif  playerguess > 100:
            print("That Guess Doesn't Fit The Criteria")
        elif playerguess < 1:
            print("That Guess Doesn't Fit The Criteria")
    else:
        print("Sorry you have run out of tries.")
        print("The correct number was",correctnumber)
        print("Want to play again?")



if __name__ == "__main__":
    main()