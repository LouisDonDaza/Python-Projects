# Ask user
import random
pie = [1,2,3,4]
random.shuffle(pie)
print(pie)
suits = ('Diamond ◆', 'Clubs ♣', 'Hearts ♥', 'Spades ♠')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
values['Three']
#print(suits[0][0].lower())
class Card():
    #Three attributes: suits, ranks and values
    def __init__(self, suit='Glitter', rank='X'):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit
#-------------------------------------------------------------------------------------
class Deck():
    '''
    Create a deck with card objects for each rank and suit
    '''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def shuffleDeck(self):
        random.shuffle(self.deck)
    def deal(self):
        #Hi
        '''
        Take top card from Deck
        '''
        return self.deck.pop(0)
    def isShort(self):
        if len(self.deck) <= 6:
            print('Getting new deck')
            self.deck.clear()
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit,rank))
            random.shuffle(self.deck)
#-------------------------------------------------------------------------------------

class Hand():
    '''
    Create a hand object to store cards and keep track of value and no. of aces
    '''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        self.cards.append(card)
        cardValue = values[card.rank]
        self.value = self.value + cardValue
        if card.rank == 'Ace':
            self.aces += 1
    def clearHand(self):
        self.cards.clear()
        self.value = 0
    def adjust_for_ace(self):
        '''
        If value of Hand is more than 21, turn the value of an Ace to a one
        '''
        if self.aces > 0 and self.value > 21:
            self.aces -= 1
            self.value -= 10
#-------------------------------------------------------------------------------------

class Chips():
    '''
    Amount player has to bet. Player cannot bet more than his available chips
    '''
    def __init__(self, total =100):
        self.total = total
        self.bet = 0
    def place_bet(self):
        noError = True
        while noError:
            try:
                self.bet = int(input('How much do you want to place for a bet?'))
            except:
                print('Input was not a number. Try again.')
            else:
                if self.bet <= self.total:
                    self.total -= self.bet
                    noError = False
                    print(f'Remaining chips: {self.total}')
                    return self.bet
                else:
                    print(f'Input was greater than available chips of {self.total}. Pls enter again')
    def win_bet(self):
        self.total = self.total + self.bet + self.bet
        print(f'You gained {self.bet} chips')
    def lose_bet(self):
        print(f"You lost {self.bet} chips")
#-------------------------------------------------------------------------------------

def hit(deck, hand):
    '''
    If player or dealer wants another card, will adjust ace if hand is greater than 21
    '''
    baraha = deck.deal()
    print(f'Your card drawn is {baraha}')
    hand.add_card(baraha)
    hand.adjust_for_ace()
def hit_or_stand(deck, hand):
    global processing
    while True:
        choice = input('Hit or Stand?')
        if choice[0].upper() == 'H':
            hit(deck, hand)
            break;
        elif choice[0].upper() == 'S':
            processing = False
            break;
        else:
            print('Input invalid. Choice is only to Hit or Stand. One more time')
#-------------------------------------------------------------------------------------

def show_some(player,dealer):
    '''
    To be used at the start so that dealer can keep one card hidden
    '''
    print('Dealer has a ')
    print(dealer.cards[0])
    print('Player has ' + str(player.value))
def show_all(player,dealer):
    '''
    To be used at the end so that dealer can reveal one card hidden
    '''
    print('Dealer has ' + str(dealer.value))
    print('Player has ' + str(player.value))
#-------------------------------------------------------------------------------------

def player_busts(pValue):
    if pValue > 21:
        print('Player bust!')
        return True
    else:
        return False
def player_win(pValue, dValue):
    if (pValue > dValue and pValue <=21) or (dValue > 21 and pValue <=21):
        print('Player wins')
        return True
    elif pValue == dValue:
        print('Draw')
        return True
    else:
        return False
def dealer_busts(dValue):
    if dValue > 21:
        print('Dealer bust!')
        return True
    else:
        return False
def dealer_win():
    #print('Dealer wins')
    pass
def push():
    pass
#-------------------------------------------------------------------------------------
# Main block of code

#from IPython.display import clear_output
print('Welcome to Black Jack, amigo!\nThe show will now begin')
newDeck = Deck()
newDeck.shuffleDeck()
playerHand = Hand()
dealerHand = Hand()
asking = True
while asking:
    chipPrompt = input('How many chips do you want to start with?\n1-100\n2-Other amount')
    if chipPrompt == '1':
        playerChips = Chips()
        asking = False
    elif chipPrompt == '2':
        while True:
            try:
                chipAmt = int(input('Enter amount of chips you want to start with'))
            except:
                print('Value entered was not a whole number. Try again')
            else:
                playerChips = Chips(chipAmt)
                break;
        asking = False
    else:
        print('Enter either 1 or 2 only pls.')
playing = True
while playing:
    print(f'Deck has {len(newDeck.deck)} cards')
    print(f'You have {playerChips.total} chips')
    playerChips.place_bet()
    playerHand.add_card(newDeck.deal())
    playerHand.add_card(newDeck.deal())
    dealerHand.add_card(newDeck.deal())
    dealerHand.add_card(newDeck.deal())
    processing = True
    while processing:
        show_some(playerHand, dealerHand)
        hit_or_stand(newDeck, playerHand)
        if player_busts(playerHand.value):
            playerChips.lose_bet()
            processing = False
    show_all(playerHand, dealerHand)
    while dealerHand.value < 17:
        hit(newDeck, dealerHand)
        show_all(playerHand, dealerHand)
    if dealer_busts(dealerHand.value):
        pass
    if player_win(playerHand.value,dealerHand.value):
        playerChips.win_bet()
    else:
        print('Dealer wins')
        playerChips.lose_bet()
    while True:
        playAgain = input('Do you want to play again? Yes or No?')
        if playAgain[0].upper() == 'Y':
            break
        elif playAgain[0].upper() == 'N':
            playing = False
            print('Thank you come again')
            break
        else:
            print('Invalid input. Yes or No')
    playerHand.clearHand()
    dealerHand.clearHand()
    #clear_output()