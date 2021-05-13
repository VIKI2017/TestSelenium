"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/7 4:02 下午'
"""
# 启动app，停止app， 重启app
import yaml
# from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from page.basepage import BasePage
import pytest


with open("../data/config.yml") as f:
    data = yaml.safe_load(f)
    baseurl = data['data']['URL']
    user = data['data']['user']
    code = data['data']['code']


def login():


class test_login(BasePage):
    def setup(self):
        self.driver = webdriver.Chrome().get(baseurl)

    def teardown(self):
        # 重启app
        self.driver.quit()

