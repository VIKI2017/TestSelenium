
from selenium.webdriver.common.by import By
from page.basepage import BasePage
import yaml
import time


with open("../data/config.yml") as f:
    data = yaml.safe_load(f)
    baseurl = data['data']['URL']

class LoginPage(BasePage):


    def login(self):
        self.parse("../data/loginpage.yml","goto_login")








