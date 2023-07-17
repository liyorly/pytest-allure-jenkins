
from pytestJenkins.WebDriverUtil import GetWebDriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWebDriver:

    #根据id选择元素
    def testCSSSELECTOR_01(self):
        wd = GetWebDriver().getChromeWebDriver()
        wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
        wd.implicitly_wait(5)
        #根据CSS_SELECTOR通过id选择文本框元素
        element = wd.find_element(By.CSS_SELECTOR,'#searchtext')
        element.send_keys('好的123')

        time.sleep(5)

    #根据class选择元素
    def testCSSSELECTOR_02(self):
        wd = GetWebDriver().getChromeWebDriver()
        wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
        #根据CSS_SELECTOR通过class选择元素
        elements = wd.find_elements(By.CSS_SELECTOR,'.plant')
        for item in elements:
            print(item.text)

    #选择子元素和后代元素
    def testCSSSELECTOR_03(self):
        wd = GetWebDriver().getChromeWebDriver()
        wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
        #根据 > 选择子元素
        element=wd.find_element(By.CSS_SELECTOR,'#container>div>div>span')
        print(element.text)
        #根据   选择后代元素
        element=wd.find_element(By.CSS_SELECTOR,'#container>div:nth-child(2)>div span')
        print(element.text)
        # 根据属性选择元素[]
        element=wd.find_element(By.CSS_SELECTOR,'[href="http://www.miitbeian.gov.cn"]')
        print(element.get_attribute('outerHTML'))

    #选择子节点元素
    def testCSSSELETOR_04(self):
        wd = GetWebDriver().getChromeWebDriver()
        wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')
        #选择第2个且是span类型的子元素
        elements=wd.find_elements(By.CSS_SELECTOR,'span:nth-child(2)')
        for item in elements:
            print(item.get_attribute('outerHTML'))

        #选择倒数第1个且是p类型的子元素
        elements=wd.find_elements(By.CSS_SELECTOR,'p:nth-last-child(1)')
        for item in elements:
            print(item.get_attribute('outerHTML'))

        #选择所有span类型的第2个节点元素
        elements=wd.find_elements(By.CSS_SELECTOR,'span:nth-of-type(2)')
        for item in elements:
            print(item.get_attribute('outerHTML'))

        #选择所有span类型的倒数第2个节点元素
        elements=wd.find_elements(By.CSS_SELECTOR,'span:nth-last-of-type(2)')
        for item in elements:
            print(item.get_attribute('outerHTML'))

        #选择p类型的偶数节点元素
        elements=wd.find_elements(By.CSS_SELECTOR,'p:nth-child(even)')
        for item in elements:
            print(item.get_attribute('outerHTML'))

        #选择p类型的奇数节点元素
        elements=wd.find_elements(By.CSS_SELECTOR,'p:nth-child(odd)')
        for item in elements:
            print(item.get_attribute('outerHTML'))


    #frame切换
    def testCSSSELECTOR_05(self):
        wd = GetWebDriver().getChromeWebDriver()
        wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')
        #切换至frame
        wd.switch_to.frame('frame1')
        elements=wd.find_elements(By.CSS_SELECTOR,'.plant')
        for item in elements:
            print(item.text)

        #切出frame
        wd.switch_to.default_content()

    #窗口切换
    def testCSSSELECTOR_06(self):
        wd = GetWebDriver().getChromeWebDriver()
        wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

        #保存当前页面
        mainWindow=wd.current_window_handle
        #点击跳转按钮
        wd.find_element(By.TAG_NAME,'a').click()
        #切换至新窗口
        for handle in wd.window_handles:
            #切换新窗口
            wd.switch_to.window(handle)
            if '必应' in wd.title:
                print('切换窗口成功！！！')
                break
        #切换回原窗口
        wd.switch_to.window(mainWindow)
        print('已切回原窗口！！！')

