"""
 Hello 

"""
from selenium import webdriver


class pySelenium():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')

    # 打开url
    def openUrl(self, url):
        self.driver.get(url)

    def switch(self, value):
        self.driver.switch_to.frame(value)


    def Qswitch(self):
        self.driver.switch_to.default_content()

    # 查找元素
    def findElement(self, by, value):
        if by == 'id':
            element = self.driver.find_element_by_id(value)
            return element
        elif by == "name":
            element = self.driver.find_element_by_name(value)
            return element
        elif by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
            return element
        elif by == 'classname':
            element = self.driver.find_element_by_class_name(value)
            return element
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(value)
            return element
        elif by == 'link_text':
            element = self.driver.find_element_by_link_text(value)
            return element
        elif by == "tag":
            element = self.driver.find_element_by_tag_name(value)
            return element
        else:
            print("无对应的方法，请检查")
            return None

    # 给指定的元素发送值
    def senKey(self, by, value, keys):
        element = self.findElement(by, value)
        element.send_keys(keys)

    # 点击事件
    def clinkElement(self, by, value):
        element = self.findElement(by, value)
        return element

    # 获取标题
    def getTitle(self):
        return self.driver.title

    def getText(self):
        pass

    # 退出
    def quit(self):
        self.driver.quit()
