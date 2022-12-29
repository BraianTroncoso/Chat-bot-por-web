import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+543571638693')
sleep(20)

with open ('spam.txt', 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press('enter')

# Otra manera de obtener lo mismo es con el siguiente codigo

"""
import pywhatkit

from datetime import datetime
import time


# Obtenemos los segundos actuales
seconds = time.time() + 60

# Transformamos los segundos a una fecha, para que sea mas fácil manipular el tiempo
date = datetime.fromtimestamp(seconds)

pywhatkit.sendwhatmsg("+543571638693", "Que onda", date.hour, date.minute)

time.sleep(5)
"""