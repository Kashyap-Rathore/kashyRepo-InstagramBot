from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?hl=en')
        time.sleep(6)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(6)

    def like_post(self, username, numberofposts):
        bot = self.bot
        bot.get('https://www.instagram.com/'+username+'/?hl=en')
        time.sleep(6)
        post = bot.find_element_by_class_name('eLAPa').click()
        time.sleep(3)
        like = bot.find_element_by_css_selector('.fr66n > button:nth-child(1)').click()
        for i in range(numberofposts):
            nextpost = bot.find_element_by_class_name('HBoOv').click()
            time.sleep(3)
            like = bot.find_element_by_css_selector('.fr66n > button:nth-child(1)').click()

instaid= input('Enter your instagram id: ')
instaidpass= input('Enter your instagram id password: ')
instaidofuser= input('Enter your instagram id of person you want to like the posts: ')
numberofposts= int(input('Enter the number of posts you want to like: '))

ed = InstagramBot(instaid, instaidpass)
ed.login()
ed.like_post(instaidofuser,numberofposts)
