import random

money = 100

#Write your game of chance functions here
def cho_han():
    #Variable Initialization
    bet = 0
    guess = None
    global money
    play_again = None

    #Get user input for guess and bet
    bet = int(input("Please enter the amount you wish to bet: "))
    guess = str(input("Please try to guess if dice roll will be odd or even:"))

    #Dice rolling mechanism
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)

    #This determines if the two rolls added together is odd or even
    #and has win/lose game logic
    sum = num1 + num2
    if sum % 2 == 0 and guess == "even":
        print(sum)
        print("The roll is even.")
        print("You win!")
        money = money + bet
        print("You now have " + str(money) + " money.")
    elif sum % 2 == 1 and guess == "odd":
        print(sum)
        print("The roll is odd.")
        print("You win!")
        money = money + bet
        print("You now have " + str(money) + " money.")
    elif sum % 2 == 0 and guess == "odd":
        print(sum)
        print("The roll is odd.")
        print("You lose!")
        money = money - bet
        print("You now have " + str(money) + " money.")
    elif sum % 2 == 1 and guess == "even":
        print(sum)
        print("The roll is even.")
        print("You lose!")
        money = money - bet
        print("You now have " + str(money) + " money.")
    
    #Play again mechanism
    play_again = input("Do you want to play again? Y or N: ")
    if play_again == "y" and money > 0:
        cho_han()
    elif play_again == "y" and money <= 0:
        print("You are out of money.")
        print("Goodbye!")
        exit()
    else:
        exit()

#Call your game of chance functions here
cho_han()