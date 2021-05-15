import yaml
from selenium import webdriver

import pytest



#
with open("/var/jenkins_home/workspace/TestSelenium/data/config.yml") as f:
    data = yaml.safe_load(f)
    baseurl = data['data']['URL']





driver = None
def get_driver():
    chrome_capabilities = {
        "browserName": "chrome",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
        "webdriver.chrome.driver": 'chromedriver'
    }


    global driver

    if driver is None:
        # driver = webdriver.Chrome()
        driver = webdriver.Remote('http://172.17.0.2:4444/wd/hub',desired_capabilities=chrome_capabilities)
        driver.get(baseurl)
        driver.maximize_window()


    return driver


@pytest.fixture(scope='session',autouse=True)
def browser():

    yield get_driver()













