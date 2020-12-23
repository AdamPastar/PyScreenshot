from pynput import keyboard
import pyautogui
import os, os.path
import sys

#styles
from colorama import init, Fore

init(convert=True)

print(f'{Fore.WHITE}Press "PrintScreen" to Take Screenshot')

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.print_screen}
]

# The currently active modifiers
current = set()

def execute():

    DIR = 'Screenshots'

    folder_files_count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    file = open("txt.txt","w+")

    file.write(str(folder_files_count))

    file.close()

    fileObject = open("txt.txt", "r")
    data = fileObject.read()

    act = int(data) + 1

    fileObject.close()

    os.remove("txt.txt")

    f = open("txt.txt","w+")

    f.write(str(act))

    f.close()

    if str(act) == "1":
        screenshot = pyautogui.screenshot("Screenshots/Screenshot(1).png")
    else:
        screenshot = pyautogui.screenshot("Screenshots/Screenshot(" + str(act) + ").png")
    print(Fore.GREEN + "Success! Screenshot Saved In: " + "Screenshots/Screenshot(" + str(act) + ").png")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()