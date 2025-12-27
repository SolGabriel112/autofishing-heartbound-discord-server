import pyautogui
import time
import ctypes
#the command to run it it case you have multiple python version installed
"py -3.12 .\fishing.py"
ctypes.windll.user32.SetProcessDPIAware()
pyautogui.FAILSAFE = True

print("Waiting for button...")
pressed = False


for i in range(200):
    while pressed != True:
        try:
            loc = pyautogui.locateCenterOnScreen("clickme.png", confidence=0.8)
            if loc:
                print("Button found at:", loc)
                pyautogui.moveTo(loc, duration=0.1)
                time.sleep(0.15)
                pyautogui.click()
                print("Clicked!")
                print("fished",i+1,"times")
                time.sleep(1.4)
                pyautogui.scroll(-100)  # scroll down 10 "clicks"
                time.sleep(0.17)
                pyautogui.write(',')
                time.sleep(0.17)
                pyautogui.write('f')
                time.sleep(0.17)
                pyautogui.press('enter')
                time.sleep(0.67)
                pressed = True
                
            else:
                print("Button not found, waiting...")
                time.sleep(0.5)
        except pyautogui.ImageNotFoundException:
            print("Button not on screen yet...")
            time.sleep(0.5)
    pressed = False
