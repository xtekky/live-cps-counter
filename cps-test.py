from pynput.mouse import Listener
from datetime import datetime, timedelta
import time

print('''
 ██████╗██╗     ██╗ ██████╗██╗  ██╗  ████████╗███████╗███████╗████████╗
██╔════╝██║     ██║██╔════╝██║ ██╔╝  ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██║     ██║     ██║██║     █████╔╝█████╗██║   █████╗  ███████╗   ██║   
██║     ██║     ██║██║     ██╔═██╗╚════╝██║   ██╔══╝  ╚════██║   ██║   
╚██████╗███████╗██║╚██████╗██║  ██╗     ██║   ███████╗███████║   ██║   
 ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝   ╚══════╝╚══════╝   ╚═╝   
     
 Credits to: https://github.com/xtekky    
''')

raw_clicks = 0
sec = int(input('How long do you want the test to be? '))
print('Click to start')
print('')

def on_click(x, y, button, pressed):
    global start
    listener.stop()
    start = time.time()
    print('- started time -')

with Listener(on_click=on_click) as listener:
    listener.join()


def on_click(x, y, button, pressed):
    global raw_clicks
    global sec
    global start
    print("\r", end="")
    raw_clicks = raw_clicks + 1
    print(raw_clicks/2, 'clicks', end="")
    if time.time() - start > sec:
        listener.stop()
        print('')
        print('- stopped time -')

with Listener(on_click=on_click) as listener:
    listener.join()

print("\r", end="")
print('')
print('You made', int(raw_clicks/2), 'Clicks in', sec, 'seconds')
raw_raw = (raw_clicks/2)
print('Your clicking speed is', raw_raw/sec, 'cps')

#EXAMPLE OUTPUT
'''
How long do you want the test to be? 10
Click to start
- started time -
164.5 clicks
- stopped time -

You made 164 Clicks in 10 seconds
Your clicking speed is 16.4 cps
'''

