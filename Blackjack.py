#G3 Interactive Python
#6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.handcard = []

    def __str__(self):
        handstr = ""
        for c in self.handcard:
            handstr = handstr +" "+ str(c)
        return "Hand contains" + handstr
            
    def add_card(self, card):
        self.handcard.append(card)

    def get_value(self):
        global VALUES
        ace= 0
        hand_value=0
        
        for c in self.handcard:
            if c.get_rank() == 'A':
                ace+=1
            hand_value += VALUES[c.get_rank()]
        if ace>0 and hand_value+10 <= 21:
            hand_value+=10
            return hand_value
        else: 
            return hand_value
               
                
    def draw(self, canvas, pos):
        for z in self.handcard:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(z.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(z.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + 73 * self.handcard.index(z), pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define deck class 
class Deck:
    def __init__(self):
         self.deckcard = [Card(str(suit),str(rank)) for suit in SUITS for rank in RANKS ]
         
    def shuffle(self):
        random.shuffle(self.deckcard)

    def deal_card(self):
        deal = self.deckcard.pop(0)
        return deal
    
    def __str__(self):
        deckstr = ""
        for c in self.deckcard:
            deckstr = deckstr +" "+ str(c)
        return "Deck contains" + deckstr



#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, in_deck,score
    
    in_deck = Deck()
    in_deck.shuffle()
    player = Hand()
    player.add_card(in_deck.deal_card())
    player.add_card(in_deck.deal_card())
    
    dealer = Hand()
    dealer.add_card(in_deck.deal_card())
    dealer.add_card(in_deck.deal_card())
    if in_play:
        score -= 1
    outcome = 'Hit or stand?'
    in_play = True    
        
   
    

def hit():
    global outcome, in_play, player, score
    player.add_card(in_deck.deal_card())
    if player.get_value() <= 21:
        outcome = "Hit or stand?"
    else:
        outcome = "You've Busted.New deal?"
        in_play = False
        score -= 1
        return score, outcome, in_play
    
def stand():
    global outcome, in_play, player,dealer, score
    if  player.get_value() >= 21:
         outcome = "You've busted,Dealer wins. New deal?"
         in_play = False
         score -= 1
         return score, outcome, in_play
    else:
        while dealer.get_value() < 17:
             dealer.add_card(in_deck.deal_card())
        else:
            if dealer.get_value() >= 21:
                outcome = "Dealer went busted and you win! New deal?"
                score += 1
                return score, outcome, in_play
            elif player.get_value() <= dealer.get_value():
                outcome = "Dealer wins. New deal?"
                score -= 1
                return score, outcome, in_play
            elif player.get_value() > dealer.get_value():
                outcome = "You win! New deal?"
                score += 1
                return score, outcome, in_play
                
   
    
# draw handler    
def draw(canvas):
    
    player.draw(canvas, [0, 300])
    dealer.draw(canvas, [0, 100]) 
    canvas.draw_text("Dealer",[30,80],20,"Black")
    canvas.draw_text("BlackJack",[250,50],35,"Black")
    canvas.draw_text("Score: "+str(score),[50,50],20,"Black")
    canvas.draw_text(outcome,[150,80],20,"Black")   
     
    canvas.draw_text("Player",[30,280],20,"Black")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_SIZE) 
    
    
    
    
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric