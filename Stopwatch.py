#G3 Interactive Python
#Mini-project #3 Stopwatch
import simplegui
import time

# define global variables

val =0
exact_stop=0
click_stop=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    A,B,C,D=0,0,0,0
    
    if t<=9:
        
        return '0' + ':' + '0' +'0'+'.'+str(t)
        
    elif t<=99:
        D = t%10
        C = t/10
        
        return  '0' + ':' + '0' +str(C)+'.'+str(D)
    
    elif t<=599:
        D = t % 10
        temp = t / 10
        C = temp % 10
        B = temp / 10
        return  '0' + ':' + str(B) +str(C)+'.'+str(D)
    
    
    elif t<=6000:
        D = t % 10
        C = (t / 10) % 10
        B = (t/100) % 6
        A = (t/10)/60
        
        return  str(A) + ':' + str(B) +str(C)+'.'+str(D)
    
    else:
        return 'Sorry!Reset!'
    
    
        
    
     
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_watch():
    timer.start()
    
    
    
def stop_watch():
   
    global exact_stop,click_stop
    if timer.is_running():
         timer.stop()
         click_stop+=1
    if val % 10==0 :
        exact_stop+=1
    

def reset_watch():
    timer.stop()
    global val,exact_stop,click_stop
    val=0
    exact_stop=0
    click_stop=0
     
    

    


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global val
    val=val+1
    return val
    


# define draw handler
def draw_handler(canvas):
    
    canvas.draw_text(format(val), (100, 120), 50, 'Red')
    canvas.draw_text(str(exact_stop)+' / '+str(click_stop), (340, 30), 25, 'White')
    

# create frame
frame = simplegui.create_frame('Stopwatch', 400, 200)
    
    
# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
start = frame.add_button('Start',start_watch,100)
stop = frame.add_button('Stop',stop_watch,100)
reset = frame.add_button('Reset',reset_watch,100)

# start frame
frame.start()    
    
     
  










