# from testcase.test_login import TestLogin
from time import sleep
import allure
from page.chrome import Chrome
import pytest

# from testcase.conftest import AestChrome
from page.chrome import Chrome
from testcase.conftest import get_driver
import time


@allure.feature("网点模块")
class TestDemo2:

    def setup_class(self):
        # self.chrome = AestChrome()
        print("初始化啦-----------")
        self.chrome = Chrome()
        self.driver = get_driver()

    @pytest.mark.run(order=1)
    @allure.story("登录")
    @allure.step("成功登录")
    def test_alogin(self,browser):
        # self.chrome.start().goto_main().login().creat_company()
        #self.chrome.goto_main().goto_login().login()
        self.chrome.goto_main(browser).goto_login().login()
        time.sleep(8)


    def test_bhaha(self):
        print("我是第二条测试用例")
        time.sleep(8)
    def test_chaha(self):
        print("我是第三条测试用例")
        time.sleep(8)



    def teardown_class(self):
        # 退出
        # driver = browser()
        print("开始关闭浏览器啦-------------")
        self.driver.quit()




