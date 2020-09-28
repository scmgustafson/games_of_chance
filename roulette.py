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
                    if guess_type == "color":
                        guess = input("Please select red or black: ")
                    elif guess_type == "odd or even":
                        guess = input("Please select odd or even: ")
                    elif guess_type == "number":
                        guess = input("Please select a number between 1 and 36 or 0 or 00: ")
                        if guess == "0":
                            guess = 37
                        elif guess == "00":
                            guess = 38
                        guess = int(guess)
            elif bet > money:
                print("That bet is more money than you have.")
                print("Please bet again.")
                card_draw()
            else:
                print("That is not a valid bet.")
                print("Please bet again.")
                card_draw()
        except:
            print("That is not a valid bet.")
            print("Please bet again.")
            card_draw()

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
        color = None
        odd_even = None
    elif spin == 38:
        color = None
        odd_even = None
    
    #Debugging info
    print(guess)
    print(type(guess))
    print(spin)
    print(color)
    print(odd_even)

#Call functions here
roulette()
