from pynput.mouse import Listener
from datetime import datetime, timedelta
import time

#assigning variables for click and cps time length
raw_clicks = 0
sec = 2
print('Click to start')


#function to start code by a click
def on_click(x, y, button, pressed):
    global start
    listener.stop() #stopping 1st listener
    start = time.time() #starting timer
    print('- started time -')
with Listener(on_click=on_click) as listener: 
    listener.join()


#looping the cps_counter function
while True:
    def cps_counter(x, y, button, pressed):
            global raw_clicks
            global sec
            global start
            raw_clicks = raw_clicks + 1 #every click, add 1 to raw click
            if time.time() - start > sec: #make script stop after 'sec' seconds to get a new value
                listener.stop() #stopoping listener
                raw_raw = (raw_clicks / 2) #dividing raw clicks because pynput counts clickand release so the clicks are double
                print("\r", end="")
                print(raw_raw/sec, 'cps', end="") #printing cps
                raw_clicks = 0 #resetting click count
                start = time.time() #restarting timer
    with Listener(on_click=on_click) as listener:
        listener.join()

