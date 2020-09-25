import random

money = 100

#Write functions here
def card_draw():
    #Variable Initialization
    global money
    bet = 0
    guess = None
    play_again = None

    #Get player input for bet and guess
    bet = int(input("Please enter the amount you wish to bet: "))
    print("Please try to guess which card will be higher.")
    guess = str(input("card1 or card2: "))

    #This builds the "deck"
    ## suits = ["spades","clubs","hearts","diamonds"]
    faces = {2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"}

    deck = []
    for face in faces:
        deck.append((face))
    
    #This pulls the first card from the deck and "removes" it
    #until deck is "shuffled"
    card1 = random.choice(deck)
    deck.remove(card1)

    #This pulls card #2
    #Not removing its value from the deck because it does not need to be
    card2 = random.choice(deck)

    #Flavor/debugging text
    print("The first card is a: " + str(card1))
    print("The second card is a: " + str(card2))

    #This takes any "face" card and gives it an equivalent integer value
    #used for comparing the 2 cards
    if card1 == "jack" or card1 == "queen" or card1 == "king":
        card1 = 10
    elif card1 == "ace":
        card1 = 11

    if card2 == "jack" or card2 == "queen" or card2 == "king":
        card2 = 10
    elif card2 == "ace":
        card2 = 11
    
    #This compares the 2 cards and awards/takes money
    if card1 > card2 and guess == "card1":
        print("The first card is higher.")
        print("You win!")
        money = money + bet
        print("You now have " + str(money) + " money.")
    elif card2 > card1 and guess == "card2":
        print("The second card is higher.")
        print("You win!")
        money = money + bet
        print("You now have " + str(money) + " money.")
    elif card1 == card2:
        print("Draw!")
        print("Your money has been returned.")
        print("You now have " + str(money) + " money.")
    elif card1 > card2 and guess == "card2":
        print("The first card is higher.")
        print("You lose!")
        money = money - bet
        print("You now have " + str(money) + " money.")
    elif card2 > card1 and guess == "card1":
        print("The second card is higher.")
        print("You lose!")
        money = money - bet
        print("You now have " + str(money) + " money.")

    #Play again mechanism
    play_again = input("Do you want to play again? Y or N: ")
    if play_again == "y" and money > 0:
        card_draw()
    elif play_again == "y" and money <= 0:
        print("You are out of money.")
        print("Goodbye!")
        exit()
    else:
        print("Goodbye!")
        exit()

#Call functions here
card_draw()