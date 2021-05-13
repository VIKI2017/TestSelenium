
from selenium.webdriver.common.by import By
from page.basepage import BasePage
from page.loginpage import LoginPage


class MainPage(BasePage):

    def goto_login(self):
        print("进登录了--------------")
        return LoginPage(self.driver)




    def find_main_page(self):
        return self.is_element_exists(*self.main_page)





