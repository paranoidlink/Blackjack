import random

def create_deck():
    return ["Ace", "Ace", "Ace", "Ace", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, "King", "King", "King", "King", "Queen", "Queen", "Queen", "Queen", "Jack", "Jack", "Jack", "Jack"]

deck = create_deck()

playerCards = []
dealerCards = []

def find_total(hand):
    total = 0
    for card in hand:
        if type(card) == int:
            #Check if a card is an int, if it is we can take it's value litteraly
            total += card
        elif card != "Ace":
            #if a card is not an int and not an ace it must be a king, queen or jack, who all have a value of 10
            total += 10
        elif total + 10 > 21:
            #Any card that makes it to this point must be an ace so we check if it's value should be 10 or 1 based on what the total of the hand is
            total += 1
        else:
            total += 10
    return total

def setup():
#Handles start of game setup, such as creating the deck, drawing the first 2 cards for the dealer and player and annoucning one of the dealers cards as well as both the players cards
    deck
    playerCards.clear()
    dealerCards.clear()
    playerCards.append(deck.pop(random.randint(0,len(deck)) - 1))
    playerCards.append(deck.pop(random.randint(0,len(deck)) - 1))
    dealerCards.append(deck.pop(random.randint(0,len(deck)) -1 ))
    dealerCards.append(deck.pop(random.randint(0,len(deck)) -1 ))

    print("You have " + str(playerCards) + "For a total of " + str(find_total(playerCards)))
    print("Dealer has " + str(dealerCards[0]))

def hit():
    playerCards.append(deck.pop(random.randint(0,len(deck)) - 1))

def bustCheck(hand):
    total = find_total(hand)
    if total > 21:
        return True

def playerTurn(hand):
    print("Would you like to hit or fold")
    usrInput = ""
    usrInput = str(input())
    if usrInput == "hit":
        hit()
        playerBust = bustCheck(playerCards)
        if playerBust == True:
            print("You drew " + str(playerCards[-1]) + " Your total is now " +str(find_total(playerCards)) + " You're Bust")
            return False
        else:
            print ("You drew " + str(playerCards[-1]) + " Your total is now " + str(find_total(playerCards)))
            return True
    elif usrInput == "fold":
      return False

def delaerTurn(hand):
    while find_total(dealerCards) <= 17:
        #makes the dealer constantly draw cards until they either go bust or hit 17 or above where they will stand
        dealerCards.append(deck.pop(random.randint(0,len(deck)) - 1))
        print ("Dealer drew " + str(dealerCards[-1]) + " Dealer total is now " + str(find_total(dealerCards)))

def findWinner(playerHand, dealerHand):
    #figures out who has the highest number below 21 or if one is above 21 and one isn't and declares the winner
    if find_total(dealerCards) > find_total(playerCards) and find_total(dealerCards) <= 21:
        print("Dealer wins with a total of " + str(find_total(dealerCards)))
    elif find_total(playerCards) > find_total(dealerCards) and find_total(playerCards) <= 21:
        print("You win with a total of" + str(find_total(playerCards)))
    elif find_total(playerCards) == find_total(dealerCards):
        print("Draw")
    elif find_total(playerCards) > 21 and find_total(dealerCards) > 21:
        print("Both Bust Draw")
    elif find_total(playerCards) > 21 and find_total(dealerCards) <= 21:
        print("You went bust dealer wins")
    elif find_total(dealerCards) > 21 and find_total(playerCards) <= 21:
        print("Dealer Bust you win")

while True:
    #makes the program loop until it closed
    print("Welcome to Blackjack!")
    setup()
    pturn = True
    while pturn == True:
        #will constantly ask the player to hit or fold until they either fold or go bust
        pturn = playerTurn(playerCards)
    delaerTurn(dealerCards)
    findWinner(playerCards, dealerCards)
        

