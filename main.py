from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
import time

chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()


driver.get("https://elgoog.im/dinosaur-game/")
time.sleep(3)
pyautogui.press("up")


while True:
    if pyautogui.pixelMatchesColor(430, 710, (33, 33, 33), tolerance=50) or\
            pyautogui.pixelMatchesColor(430, 676, (33, 33, 33), tolerance=50) or\
            pyautogui.pixelMatchesColor(430, 601, (33, 33, 33), tolerance=50):
        pyautogui.press("space")