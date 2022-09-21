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
            total += card
        elif card != "Ace":
            total += 10
        elif total + 10 > 21:
            total += 1
        else:
            total += 10
    return total



def setup():
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


def fold():
    return True

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
        dealerCards.append(deck.pop(random.randint(0,len(deck)) - 1))
        print ("Dealer drew " + str(dealerCards[-1]) + " Dealer total is now " + str(find_total(dealerCards)))

def findWinner(playerHand, dealerHand):
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
    print("Welcome to Blackjack!")
    setup()
    pturn = True
    while pturn == True:
        pturn = playerTurn(playerCards)
    delaerTurn(dealerCards)
    findWinner(playerCards, dealerCards)
        

