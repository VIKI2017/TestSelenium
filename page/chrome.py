"""
__author__ = 'viki.wu'
__time__ = '2021/3/7 4:02 下午'
"""
# 启动app，停止app， 重启app
import yaml
from selenium import webdriver
from page.basepage import BasePage
from page.mainpage import MainPage




class Chrome(BasePage):

    def stop(self,driver):
        # 退出
        self.driver = driver
        self.driver.close()
    #
    def goto_main(self,driver):
        print("进goto_main----------------")
        return MainPage(driver)



