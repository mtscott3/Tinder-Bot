from typing import Counter
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By
from random import random

## Login to the main page:
# 1.) Run the python script or use it interactively. 
# 2.) "Bot = TinderBot()" activates the bot itself
# 3.) The "login()" function is invoked so the bot will login to tinder.
# 4.) Wait for the bot to login.

## The bot uses "auto_swipe()" function to tell the bot to continuously swipe for 45 minutes while 
## pausing a few seconds and randomly swiping right (73% of the time) or left (27% of the time) to 
## avoid Tinder's bot ban. The bot swipes every second and the counter prints out each second until 
## reaching 2700 seconds (45 minutes). you may want to get tinder plus to allow unlimited swipes 
## so the bot can reach the full 45 minutes.

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://tinder.onelink.me/9K8a/3d4abb81')
        
        sleep(5)

        fb_btn = self.driver.find_element(By.XPATH, '//button[@aria-label="Log in with Facebook"]')
        fb_btn.click()

        # Saving base window & switching to login popup.
        # (In the interactive shell use "bot.driver.window_handles" to see the multiple windows.)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Input Email/Username
        email_in = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_in.send_keys('your email')

        # input password
        pw_in = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pw_in.send_keys('your password')

        sleep(3)

        login_btn = self.driver.find_element(By.NAME, 'login')
        login_btn.click()

        self.driver.switch_to.window(self.driver.window_handles[0])

        sleep(5)

        popup_cookies = self.driver.find_element(By.XPATH, '//button[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) button--outline Bdw(2px) Bds(s) Trsdu($fast) Bdc($c-secondary) C($c-secondary) Bdc($c-base):h C($c-base):h Bdc($c-base):f C($c-base):f Bdc($c-base):a C($c-base):a Fw($semibold) focus-button-style W(100%)--s"]')
        popup_cookies.click()

        sleep(5)

        popup_1 = self.driver.find_element(By.XPATH, '//button[@aria-label="Allow"]')
        popup_1.click()

        sleep(1)

        popup_2 = self.driver.find_element(By.XPATH, '//button[@aria-label="Enable"]')
        popup_2.click()

        sleep(6)

        # Use this to clear the "are you vaccinated?" popup incase the popup comes back.
        # vax_popup = self.driver.find_element(By.XPATH, '//*[@id="u1056518897"]/div/div/div[1]/div[3]/button[2]')
        # vax_popup.click()

    def like(self):
        like_btn = self.driver.find_element(By.XPATH, '//button[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-like-green):a"]')
        like_btn.click()
    
    def dislike(self):
        dislike_btn = self.driver.find_element(By.XPATH, '//button[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-pink):a"]')
        dislike_btn.click()
    
    def auto_swipe(self):
        Counter = 0
        time_duration = 2700
        time_start = time.time()
        while time.time() < time_start + time_duration:
            Counter += 1
            print(Counter)
            sleep(1)
            try:
                rand = random()
                if rand < .73:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element(By.XPATH, '//button[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(42px)--s Mih(50px)--ml C($c-secondary) C($c-base):h Fw($semibold) focus-button-style D(b) Mx(a)"]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element(By.XPATH, '//button[@title="Back to Tinder"]')
        match_popup.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()
