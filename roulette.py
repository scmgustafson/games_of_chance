import random

money = 100

#Write functions here
def roulette():
    #Variable Initialization
    global money
    bet = 0
    guess_type = None
    guess = None
    color = None
    odd_even = None
    spin = 0
    play_again = None

    #get player input for bet and guess
    while bet == 0:
        try:
            bet = int(input("Please enter the amount you wish to bet: "))
            if bet <= money:
                while guess_type == None:
                    print("You may bet on a color, odd or even, or a number")
                    guess_type = input("Please select 'color', 'odd or even', or 'number': ")
                    if guess_type.lower() == "color":
                        guess = input("Please select red or black: ")
                    elif guess_type.lower() == "odd or even":
                        guess = input("Please select odd or even: ")
                    elif guess_type.lower() == "number":
                        guess = input("Please select a number between 1 and 36 or 0 or 00: ")
                        if guess == "0":
                            guess = 37
                        elif guess == "00":
                            guess = 38
                        guess = int(guess)
                    else:
                        print("That is not a valid game type.")
                        print("Please select again.")
                        print("--------")
                        roulette()

            elif bet > money:
                print("That bet is more money than you have.")
                print("Please bet again.")
                roulette()
            else:
                print("That is not a valid bet.")
                print("Please bet again.")
                roulette()
        except:
            print("That is not a valid bet.")
            print("Please bet again.")
            roulette()

    #Random spin on a roulette wheel
    spin = random.randint(1,38)

    #Assigns odd/even and color to the int spin
    if spin >= 1 and spin <= 10 and spin % 2 == 0:
        color = "black"
        odd_even = "even"
    elif spin >= 1 and spin <= 10 and spin % 2 == 1:
        color = "red"
        odd_even = "odd"
    elif spin >= 11 and spin <= 18 and spin % 2 == 0:
        color = "red"
        odd_even = "even"
    elif spin >= 11 and spin <= 18 and spin % 2 == 1:
        color = "black"
        odd_even = "odd"
    elif spin >= 19 and spin <= 29 and spin % 2 == 0:
        color = "black"
        odd_even = "even"
    elif spin >= 19 and spin <= 29 and spin % 2 == 1:
        color = "red"
        odd_even = "odd"
    elif spin >= 29 and spin <= 36 and spin % 2 == 0:
        color = "red"
        odd_even = "even"
    elif spin >= 29 and spin <= 36 and spin % 2 == 1:
        color = "black"
        odd_even = "odd"

    #0 and 00 spots on roulette wheel
    if spin == 37:
        color = "green"
        odd_even = None
    elif spin == 38:
        color = "green"
        odd_even = None

    #Evaluating win and bet amounts
    if guess_type.lower() == "color":
        if spin == 37:
            print("The number is... 0!")
        if spin == 38:
            print("The number is... 00!")
        elif spin != 38 and spin != 37:    
            print("The number is... " + str(spin) + "!")
        print("The color is... " + str(color) + "!")
        if guess.lower() == "red" and color == "red":
            print("You win!")
            money = money + bet
        elif guess.lower() == "black" and color == "black":
            print("You win!")
            money = money + bet
        else:
            print("You lose!")
            money = money - bet

    if guess_type.lower() == "odd or even":
        if spin == 37:
            print("The number is... 0!")
        if spin == 38:
            print("The number is... 00!")
        elif spin != 38 and spin != 37:    
            print("The number is... " + str(spin) + "!")
        if guess.lower() == "odd" and odd_even == "odd":
            print("You win!")
            money = money + bet
        elif guess.lower() == "even" and odd_even == "even":
            print("You win!")
            money = money + bet
        else:
            print("You lose!")
            money = money - bet
    
    if guess_type.lower() == "number":
        if spin == 37:
            print("The number is... 0!")
        if spin == 38:
            print("The number is... 00!")
        elif spin != 38 and spin != 37:    
            print("The number is... " + str(spin) + "!")
        if guess == spin:
            print("You win!")
            money = money + (bet * 35)
        else:
            print("You lose!")
            money = money - bet

    print("You now have " + str(money) + " money.")
    print("-----------")

    #play again mechanism
    while play_again != "y":
        play_again = input("Do you want to play again? Y or N: ")
        if play_again.lower() == "y" and money > 0:
            roulette()
        elif play_again.lower() == "y" and money <= 0:
            print("You are out of money.")
            print("Goodbye!")
            exit()
        elif play_again.lower() == "n":
            print("Goodbye!")
            exit()
        else:
            print("Please enter N or Y")
    

    #Debugging info
    

#Call functions here
roulette()
