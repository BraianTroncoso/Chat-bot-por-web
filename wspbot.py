import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+543571638693')
sleep(20)

with open ('spam.txt', 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press('enter')

