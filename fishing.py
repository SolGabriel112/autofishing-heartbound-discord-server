import pyautogui
import time
import ctypes

ctypes.windll.user32.SetProcessDPIAware()
pyautogui.FAILSAFE = True

print("Waiting for button...")
pressed = False

while True:
    while pressed != True:
        try:
            loc = pyautogui.locateCenterOnScreen("clickme.png", confidence=0.8)
            if loc:
                print("Button found at:", loc)
                pyautogui.moveTo(loc, duration=0.3)
                pyautogui.click()
                print("Clicked!")
                time.sleep(1.25)
                pyautogui.scroll(-100)  # scroll down 10 "clicks"
                time.sleep(0.15)
                pyautogui.write(',')
                time.sleep(0.15)
                pyautogui.write('f')
                time.sleep(0.15)
                pyautogui.press('enter')
                time.sleep(0.6)
                
            else:
                print("Button not found, waiting...")
                time.sleep(0.5)
        except pyautogui.ImageNotFoundException:
            print("Button not on screen yet...")
            time.sleep(0.5)
    
