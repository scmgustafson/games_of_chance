import random

money = 100

#Write your game of chance functions here
def coin_flip(bet,guess):
    # This is the coin flip mechanism
    num = random.randint(1,2)
    if num == 1:
        return "Tails"
    else:
        return "Heads"






#Call your game of chance functions here
