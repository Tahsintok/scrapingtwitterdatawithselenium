from usersinfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        
        self.browser= webdriver.Chrome()
        self.username= username
        self.password= password

    def singIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        usernameInput.send_keys(self.username)
        time.sleep(2)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(2)
        passwordInput = self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passwordInput.send_keys(self.password)
        time.sleep(2)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
    def search(self, hashtag):
        searchInput=self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(4)
        list = self.browser.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
        time.sleep(10)
        for item in list:
            print("*******")
            print(item.text)


twitter=Twitter(username,password)
twitter.singIn()
twitter.search("software")

