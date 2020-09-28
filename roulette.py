import random

money = 100

#Write functions here
def roulette():
    #Variable Initialization
    global money
    bet = 0
    guess = None
    color = None
    odd_even = None
    spin = 0
    play_again = None

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
        spin = "0"
        color = None
        odd_even = None
    elif spin == 38:
        spin = "00"
        color = None
        odd_even = None
    
    #Debugging info
    print(spin)
    print(color)
    print(odd_even)

#Call functions here
roulette()
