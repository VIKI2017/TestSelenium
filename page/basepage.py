from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import yaml
import pytest
from time import sleep


class BasePage:

    def __init__(self,driver:WebDriver=None):

        self.driver = driver
        self.timeout = 30

    #重写元素定位方法
    def find_element(self, *loc):
        driver = self.driver
        try:
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # ele = self.driver.find_element(*loc)
            ele = driver.find_element(*loc)
            return ele
        except:
            print ('Can Not Find The Element %s In Page' % loc[1])
            raise



    def is_element_exists(self, *loc):
        '''
        在15秒内判断元素是否存在
        :param loc: 定位方式
        :return:
        '''
        ele = False
        if self.driver.find_element(*loc) is not None:
            ele = True
            return ele
        else:
            return ele

    # 重写元素定位方法
    def find_elements(self, *loc):
        self.driver.implicitly_wait(5)
        eles = self.driver.find_elements(*loc)


        try:
            if len(eles):
                # length = len(self.driver.find_elements(*loc))
                # ele = self.driver.find_elements(*loc)
                return eles
        except:
            print ('Can Not Find The Element %s In Page' % loc[1])
            raise

    def find(self, locator, value):
        sleep(3)
        return self.find_element(locator, value)

    def finds(self, locator, value,index):
        result = self.driver.find_elements(locator, value)
        print("打印下list的长度："+str(len(result)))
        return self.driver.find_elements(locator,value)[index]

    def find_and_click(self, locator, value):
        self.find(locator, value).click()
        sleep(5)

    def find_and_send(self, locator, value, content):
        self.find(locator, value).send_keys(content)

    def finds_and_click(self,locator,value,index):
        # print(list_one,index)
        sleep(2)
        self.finds(locator,value,index).click()
        sleep(5)




    def finds_and_send(self, locator, value, index, content):
        # self.finds(locator, value , index).send_keys(content)
        self.find_elements(locator,value)[index].send_keys(content)

    def parse(self, yaml_path, fun_name):
        """
        解析关键字，实现相应动作
        :param yaml_path:
        :param fun_name:
        :return:
        """
        with open(yaml_path, "r", encoding="utf-8") as f:
            function = yaml.load(f,Loader=yaml.FullLoader)
            # 从关键字中取出一个函数
        steps = function.get(fun_name)
        list_ome = []

        # 解析每一组关键字
        for step in steps:
            # 如果发现关键字是 find_and_click ，就调用已经封装好的 find_and_click 即可
            if step.get("action") == "find_and_click":
                self.find_and_click(step.get('locator'), step.get('value'))
            elif step.get("action") == "find_and_send":
                self.find_and_send(step.get('locator'), step.get('value'),  step.get('content'))
            elif step.get("action") == "finds_and_click":
                self.finds_and_click(step.get('locator'),step.get('value'),step.get('index'))
            elif step.get("action") == "finds_and_send":
                self.finds_and_send(step.get('locator'), step.get('value'), step.get('index'), step.get('content'))