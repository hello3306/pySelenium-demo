"""
 Hello 

"""

import time

import pSelenium


class kst():
    def __init__(self):
        self.driver = pSelenium.pySelenium()
        self.url = "http://m.kangsitiankeji.com"

    def run(self):
        self.driver.openUrl(self.url)
        self.login()
        self.user()

    def user(self):
        self.driver.findElement("id", "RegionPanel1_leftPanel_accordionMenu_ctl01_header_hd").click()
        self.driver.findElement("id", "ext-gen1240").click()
        self.driver.switch("fnode2")
        self.driver.findElement("xpath", '//*[@id="form1"]/div[3]/ul/li[6]/a').click()
        time.sleep(1)
        self.driver.findElement("id", 'Form5_ctl00_ttbUserCode-inputEl').send_keys("18748565508")
        self.driver.findElement("id", 'ext-gen1047').click()
        time.sleep(3)
        self.driver.findElement("xpath", '//*[@id="ext-gen1762"]/div/a').click()
        self.driver.Qswitch()
        time.sleep(2)
        iframe = self.driver.findElement('xpath',
                                         "/html[@class='x-strict x-viewport']"
                                         "/body[@id='ext-gen1018']"
                                         "/form[@id='form1']"
                                         "/div[contains(@id,'f21_')]"
                                         "/div[contains(@id,'f21_')]"
                                         "/div[1]"
                                         "/iframe")
        self.driver.switch(iframe)

        self.driver.findElement("xpath", '//*[@id="ext-gen1097"]/div')

    # 登录
    def login(self):
        self.driver.findElement('id', 'LoginID').send_keys("admin")
        self.driver.findElement('id', 'PassWord').send_keys("")
        self.driver.findElement('id', 'loginbtn').click()


if __name__ == "__main__":
    c = kst()
    c.run()
