from pynput.mouse import Listener
import time

raw_clicks = 0
sec = 0.6

def on_click(x, y, button, pressed):
    global start
    listener.stop()
    start = time.time()
    print('')

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
                raw_raw = round(raw_raw/sec, 1)
                print("\r", end="")
                print(raw_raw, 'cps', end="")
                raw_clicks = 0
                start = time.time()

    with Listener(on_click=on_click) as listener:
        listener.join()







