#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random
suits = ('Diamond','Clubs','Hearts','Spades')
ranks = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
values = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}



class Cards(): 
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
        
    def __str__(self):
        return '{} of {}'.format(self.rank,self.suit)
        

    
class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))
        random.shuffle(self.deck)
        
    def __str__(self):
        for cards1 in self.deck:
            print('{}'.format(cards1))      
        
    
    
    
class Player():
    def __init__(self):
        self.hand = []
        self.cardsum = []
        self.balance = 0
        
    def bet(self): # betting function, takes int input from player and stores it as betting amount
        try:
            self.amount = int(input("How much would you like to bet: $"))
        except:
            print("invalid please enter again")
            self.bet()
        
    def hit(self,deck): # hitting function, if the player wants to receive an additional playing card
        self.hand.append(playDeck.deck[-1])
        playDeck.deck.pop()
        for cards1 in self.hand:
            print('Player 1 has the following card(s): {} '.format(cards1))
            if len(self.hand) == 1:
                print('Player 1 cards add up to: {} '.format(cards1.values))
            
    def p1choice(self): # combining the hit (and stay) functions, and checks the player's hand for busts (if player loses)
        p1choice = input('Player 1, would you like to hit or stay (type "hit" or "stay")? ')
        self.p1 = True
        self.p2 = True
        while self.p1:
            if p1choice == 'hit':
                print('\n')
                player1.hit(playDeck)
                self.cardsum = []
                for cards1 in self.hand: # want to check if player 1 busts/booms
                    self.cardsum.append(cards1.values)
                if sum(self.cardsum)<=21:
                    Ace(self.hand,self.cardsum)
                    print('Your cards add up to {}'.format(str(sum(self.cardsum))))
                else:
                    print('Your cards add up to {} - BUST, You lose!\n'.format(str(sum(self.cardsum))))
                    self.p2 = False
                    break
                p1choice = input('Would you like to hit again? (type "hit" or "stay")? ')
            elif p1choice == 'stay':
                print('\n')
                dealer.hit(playDeck)
                self.p1 = False
            else:
                p1choice = input('Please type a valid response (hit or stay): \n')
            
            
            
            
class Dealer(): 
    def __init__(self):
        self.dealer = []
        self.dealersum = []
    
    def hit(self,deck): # dealer hit function
        self.dealer.append(playDeck.deck[-1])
        playDeck.deck.pop()
        self.dealersum = []
        for cards2 in self.dealer:
            print('Dealer has the following card(s): {}'.format(cards2))
            self.dealersum.append(cards2.values)
        if sum(self.dealersum)<=21:
            Ace(self.dealer,self.dealersum)
            print('Dealer cards add up to {}\n'.format(str(sum(self.dealersum))))
        else:
            print('Dealer cards add up to {} - BUST, You win!\n'.format(str(sum(self.dealersum))))    

    def dealerplay(self): # dealer keeps hitting until dealer wins, loses, or tie
        dealercontinue = True
        while dealercontinue:
            if sum(self.dealersum)<=21 and sum(self.dealersum)<sum(player1.cardsum):
                dealer.hit(playDeck) 
            elif sum(self.dealersum)<=21 and sum(self.dealersum)>sum(player1.cardsum):
                #print('Dealer Wins, Player 1 LOSES!')
                dealercontinue = False
            elif sum(self.dealersum)==sum(player1.cardsum):
                #print('Tie!!')
                dealercontinue = False
                break
            elif sum(self.dealersum)>21:
                #print('Dealer loses, Player 1 Wins!')
                break
            else:
                print('Unexpected Occurence')

                
class Ace():
    def __init__(self,hand,hand_sum):
        self.hand = hand
        self.hand_sum = hand_sum
        for cards in self.hand:
            if cards.rank == 'A' and sum(self.hand_sum) in range (7,12):
                cards.value = 11
                hand_sum.remove(1)
                hand_sum.append(cards.value)
            else:
                continue
            
                
def check_win(): # checks either if the dealer or player wins, and declares it. Also distributes bets
    if sum(dealer.dealersum)>sum(player1.cardsum) and sum(dealer.dealersum)<= 21 and sum(player1.cardsum)<= 21:
        print('Dealer wins, you lose the bet...')
        player1.balance -= player1.amount
    elif sum(dealer.dealersum)<sum(player1.cardsum) and sum(dealer.dealersum)<= 21 and sum(player1.cardsum)<= 21:
        print('Player 1 wins, you win the bet!')
        player1.balance += player1.amount
    elif sum(dealer.dealersum)==sum(player1.cardsum) and sum(dealer.dealersum)<= 21 and sum(player1.cardsum)<= 21:
        print('Tie! No one wins')
    elif sum(dealer.dealersum)>21 and sum(player1.cardsum)<=21:
        print('Player 1 wins, you win the bet!')
        player1.balance += player1.amount
    elif sum(player1.cardsum)>21 and sum(dealer.dealersum)<=21:
        print('Dealer wins, you lose the bet...')
        player1.balance -= player1.amount 
    else:
        print('Unexpected Occurence')
    print('Player 1 Balance: {}\n'.format(player1.balance))
    
    
def playagain(): # function to ask if the player wants to play again
    play = True
    while play:
        again = input("Do you want to play again (yes,no)? ")
        if again == 'yes':
            playDeck = Deck()
            player1.hand = []
            player1.cardsum = []
            dealer.dealer = []
            dealer.dealersum = []
            main()
            print('\n')
        elif again == 'no':
            print('\nThank you for playing')
            play = False
            break
        else:
            pass
            print('\n')
    
    
def main(): # main function to tie it all in
    player1.bet()
    dealer.hit(playDeck)
    player1.hit(playDeck)
    player1.p1choice()
    if player1.p2:
        dealer.dealerplay()
    check_win()
    playagain()


# In[19]:


## Main Code

print('Welcome to Black Jack\n')
player1 = Player()
dealer = Dealer()        
playDeck = Deck()


main()


# In[ ]:




