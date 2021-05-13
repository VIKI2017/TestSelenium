from __future__ import print_function
import pytest
import allure
import os



if __name__ == '__main__':
    pytest.main()

    # pytest.main(['-s', '-q', '--alluredir', './result/', '--clean'])
    # pytest.main(['-v','--alluredir ./report'])
    # pytest.main(['-s','-q','--alluredir=../result'])
    #/var/jenkins_home/workspace/TestSelenium/allure-report
    #pytest.main(['-s','-q', '--alluredir', './result/xml', '-n=3'])
    #pytest.main(['-s', '-q', '--alluredir', '/var/jenkins_home/workspace/TestSelenium/result/xml'])
    #os.system("allure generate /var/jenkins_home/workspace/TestSelenium/result/xml -o /var/jenkins_home/workspace/TestSelenium/result/html --clean")
    #os.system("allure generate result/xml -o result/html --clean")
    # os.system(("allure serve allure"))
    #allure serve D:\LearnProject\SeleniumProject\testcase\result\xml




