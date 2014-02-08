#G3 Interactive Python
#Mini-project #5 Memory
#test comment
import simplegui
import random

def new_game():
    global deck, turns, exposed, state
    set1 = range(8)
    deck = set1 *2
    random.shuffle(deck)
    state = {1:'', 2:''}
    rect_pos = [50,60]
    exposed = [False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False]
    turns = 0
    

def click(pos):
    global rect_pos,card,exposed,state,turns
    rect_pos = list(pos)
    for i in range(len(deck)):
        if pos[0] > (i*50) and pos[0] < (i*50+50) and exposed[i]== False:
            if state[1] == '':
                exposed[i] = True
                state[1] = i
            elif state[2] == '':
                turns += 1
                exposed[i] = True
                state[2] = i
                if deck[state[1]] == deck[state[2]]:
                    state = {1:'', 2:''}
            elif state[2] != '' and state[1] != '':
                exposed[state[1]] = False
                exposed[state[2]] = False
                state[1] = i
                exposed[i] = True
                state[2] = ''  
    
def draw(canvas):
    label.set_text("Turns = " + str(turns))
    for i in range(len(deck)):
        if exposed[i]:
            canvas.draw_text(str(deck[i]),[(50*i),60],50,"red")
        else:
            canvas.draw_polygon([(i*50,0),(i*50+50,0),(i*50+50,100),(i*50,100)], 5, "black","green")
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
