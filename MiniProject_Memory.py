# http://www.codeskulptor.org/#user14_kD9mXqDZh9yRMfq.py

# implementation of card game - Memory

import simplegui
import random

CARD_NUM = 8

cards = range(CARD_NUM) + range(CARD_NUM)
exposed = [False for i in cards]
click_card_1 = -1
click_card_2 = -1
num_of_clicks = 0

# helper function to initialize globals
def init():
    global cards, exposed, click_card_1, click_card_2, num_of_clicks
    random.shuffle(cards)    
    exposed = [False for i in cards]
    click_card_1 = -1
    click_card_2 = -1
    num_of_clicks = 0
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards, exposed, click_card_1, click_card_2, label, num_of_clicks
    
    x, y = pos
    click_card = x // 50
    
    if not exposed[click_card]:
        if click_card_1 == -1:
            click_card_1 = click_card
            num_of_clicks += 1
        elif click_card_2 == -1:
            click_card_2 = click_card
        else:
            if cards[click_card_1] != cards[click_card_2]:
                exposed[click_card_1] = False
                exposed[click_card_2] = False
            click_card_1 = click_card
            click_card_2 = -1
            num_of_clicks += 1
        exposed[click_card] = True
        label.set_text("Moves = " + str(num_of_clicks))
            
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed    
    for i in range(len(cards)):
        x = i * 50
        if exposed[i]:
            canvas.draw_text(str(cards[i]), (x, 85), 100, "White")
        else:
            points = [(x, 0), (x + 50, 0), (x + 50, 100), (x, 100)]
            canvas.draw_polygon(points, 2, "Black", "Green")
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric