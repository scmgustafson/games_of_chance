import random

money = 100

#Write functions here
def card_draw():
    #Variable Initialization
    global money
    bet = 0
    guess = None
    play_again = None
    
    #This builds the "deck"
    ## suits = ["spades","clubs","hearts","diamonds"]
    faces = {2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"}

    deck = []
    for face in faces:
        deck.append((face))
    
    #This pulls the first card from the deck and "removes" it
    #until deck is "shuffled"
    card = random.choice(deck)
    deck.remove(card)

    #This pulls card #2
    #Not removing its value from the deck because it does not need to be
    card2 = random.choice(deck)

    #Flavor/debugging text
    print("The first card is a " + str(card))
    print("The second card is a " + str(card2))

    #This takes any "face" card and gives it an equivalent integer value
    #used for comparing the 2 cards
    if card == "jack" or card == "queen" or card == "king":
        card = 10
    elif card == "ace":
        card = 11

    if card2 == "jack" or card2 == "queen" or card2 == "king":
        card2 = 10
    elif card2 == "ace":
        card2 = 11
    
    #This compares the 2 cards
    if card > card2:
        print("card1 is higher")
    elif card2 > card:
        print("card2 is higher")
    elif card == card2:
        print("Draw!")

#Call functions here
card_draw()