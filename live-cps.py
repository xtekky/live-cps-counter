from pynput.mouse import Listener
from datetime import datetime, timedelta
import time

raw_clicks = 0
sec = 2
print('Click to start')


def on_click(x, y, button, pressed):
    global start
    listener.stop()
    start = time.time()
    print('- started time -')
with Listener(on_click=on_click) as listener:
    listener.join()

    
while True:
    def on_click(x, y, button, pressed):
            global raw_clicks
            global sec
            global start
            raw_clicks = raw_clicks + 1
            if time.time() - start > sec:
                listener.stop()
                raw_raw = (raw_clicks / 2)
                print("\r", end="")
                print(raw_raw/sec, 'cps', end="")
                raw_clicks = 0
                start = time.time()
    with Listener(on_click=on_click) as listener:
        listener.join()

