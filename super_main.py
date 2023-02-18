# Necessary imports for the clicking
import time
import threading
from pynput.mouse import Button, Controller
# Necessary for keyboard inputs in the program
from pynput.keyboard import Listener, KeyCode

 
# Variables necessary for the delay inbetween clicks, defining which button is getting clicked, and what buttons are 
# used
delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
 
# class used to define
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
# Checks to figure out if the program is running, also brings in outside variables
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True
# Methods to control the clicks
    def start_clicking(self):
        self.running = True
 
    def stop_clicking(self):
        self.running = False
 
    def exit(self):
        self.stop_clicking()
        self.program_run = False
# this is what defines how the clicks works 
    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
 
# Defines the mouse 
mouse = Controller()
thread = ClickMouse(delay, button)
thread.start()
 
# Defines what happens on key press 
def on_press(key):
    if key == start_stop_key:
# Says that if the start_stop key is pressed while running then the program will stop, else it will start clicking
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        thread.exit()
        listener.stop()
# Listens for key presses 
with Listener(on_press=on_press) as listener:
    listener.join()