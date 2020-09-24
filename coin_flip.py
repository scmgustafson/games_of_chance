import random

money = 100

#Write your game of chance functions here
def coin_flip():
    #Variable initilization
    bet = 0
    guess = None
    global money
    play_again = None

    #This prints out the rules of the game
    #and tells the user how much money they have currently
    print("----------------------")
    print("Let's play coin flip!")
    print("----------------------")
    print("Instructions: ")
    print("Please try to guess which side a coin lands on.")
    print("---------------------")
    print("You currently have " + str(money) + " money left.")
    print("----------------------")
    
    #This gets the user's bet amount and guess
    bet = int((input("Please enter the amount you wish to bet: ")))
    print("You have bet " + str(bet) + " money.")
    print("----------------------")
    guess = str(input("Please guess heads or tails: "))
    print("You have guessed " + str(guess) + ".")
    print("----------------------")

    #Flavor text
    print("Flipping the coin now!")
    print("----------------------")

    # This is the coin flip mechanism
    num = random.randint(1,2)
    if num == 1 and guess == "tails":
        print("The coin landed on tails.")
        print("You win " + str(bet) + "!")
        print("----------------------")
        money = money + bet
        print("You now have " + str(money) + " money.")
        print("----------------------")
    elif num == 2 and guess == "heads":
        print("The coin landed on heads.")
        print("You win " + str(bet) + "!")
        print("----------------------")
        money = money + bet
        print("You now have " + str(money) + " money.")
        print("----------------------")
    elif num == 1 and guess == "heads":
        print("The coin landed on tails.")
        print("You lose!")
        print("----------------------")
        money = money - bet
        print("You now have " + str(money) + " money.")
        print("----------------------")
    elif num == 2 and guess == "tails":
        print("The coin landed on heads.")
        print("You lose!")
        print("----------------------")
        money = money - bet
        print("You now have " + str(money) + " money.")
        print("----------------------")

    #This gets input to restart the game or not
    play_again = input("Play again? Y or N: ")
    if play_again == "y" and money > 0:
        coin_flip()
    elif play_again == "y" and money <= 0:
        print("----------------------")
        print("You are out of money!")
        print("Goodbye!")
        exit()
    else:
        print("----------------------")
        print("Goodbye!")
        exit()

#Call your game of chance functions here
coin_flip()
