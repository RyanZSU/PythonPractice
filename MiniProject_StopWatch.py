# http://www.codeskulptor.org/#user12_DSBzrrkjDqeCRc1.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
totalStop = 0
accurateStop = 0
tickCount = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t // 600
    B = (t % 600) // 100
    C = (t % 100) // 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer
    if not timer.is_running():
        timer.start()

def stop():
    global totalStop, accurateStop, timer
    if timer.is_running():
        totalStop += 1
        if tickCount % 10 == 0:
            accurateStop += 1
        timer.stop()

def reset():
    global totalStop, accurateStop, tickCount, timer
    totalStop = 0
    accurateStop = 0
    tickCount = 0
    if timer.is_running():
        timer.stop()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tickCount
    tickCount += 1

timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw_handler(canvas):
    global totalStop, accurateStop, tickCount, timer
    scoreMsg = str(accurateStop) + "/" + str(totalStop)
    canvas.draw_text(format(tickCount), (50, 120), 70, "Red")
    canvas.draw_text(scoreMsg, (210, 40), 40, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
frame.add_button("Start", start, 150)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset, 150)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
