# PyAutoGUI Demo

from turtle import clear
import pyautogui
import time

delayTime = 0.5
currentMouseX, currentMouseY = pyautogui.position()

while currentMouseX != 50000:
    currentMouseX, currentMouseY = pyautogui.position()
    print("")
    print("1 - Getting current mouse coordinates...")
    time.sleep(delayTime)

    print("")
    print("2 - Current coordinates: " +
          str(currentMouseX) + " " + str(currentMouseY))
    time.sleep(delayTime)
    print("")
    print("3 - Moving mouse to: 1000 1700 please wait...")
    pyautogui.moveTo(1000, 1700, 0.5)
    pyautogui.click()
    print("")
    print("4 - Click")

    time.sleep(delayTime)

    print("")
    print("-----------------------")

    time.sleep(delayTime)

    currentMouseX, currentMouseY = pyautogui.position()
    print("")
    print("1 - Getting current mouse coordinates...")
    time.sleep(delayTime)

    print("")
    print("2 - Current coordinates: " +
          str(currentMouseX) + " " + str(currentMouseY))
    time.sleep(delayTime)
    print("")
    print("3 - Moving mouse to: 1500 1700 please wait...")
    pyautogui.moveTo(1500, 1700, 0.5)

    pyautogui.click()
    print("")
    print("4 - Click")

    time.sleep(delayTime)

    print("")
    print("-----------------------")

    time.sleep(delayTime)
