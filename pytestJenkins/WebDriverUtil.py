import os

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

#获取webdriver
class GetWebDriver:

    def getChromeWebDriver(self):
        #获取Chrome浏览器的webdriver
        wd=webdriver.Chrome(service=Service(r''+os.getcwd()+'\chromedriver'))
        print('获取webdriver成功，',os.getcwd())
        return wd

