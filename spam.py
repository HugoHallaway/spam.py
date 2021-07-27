# 1. Open Terminal and type in : "python3 -m pip install pyautogui"
# 2. You can replace "test spam" by the sentence you want ! 
# 2.1 You can modify "enter" for user an another key !

import pyautogui as auto
from time import sleep

while True:
    auto.write('test spam')
    auto.press('enter')
    sleep(1)

# Done! Now, Have fun ! Spam your friends and be smart :) !

# If you get "no mudule named pyautogui" error, sure you use python3.
# Open Terminal and start spam.py with 'python3 spam.py'.