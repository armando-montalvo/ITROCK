from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import xlrd


class sel_exc(object):
    def __init__(self):
        self.book = xlrd.open_workbook('C:\\Users\Mario/Desktop\GIT\python\Libro1.xls')
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wd="'buscador'"

    def enter_data(self):
        for i in range(2):
            cel = self.book.sheet_by_index(0).row(i)[0].value

            # navigate to the application home page
            self.driver.get("http://www.liverpool.com.mx")
            # get the search textbox
            self.driver.find_element_by_xpath(".//*[@id=%s]"%(self.wd)).send_keys(cel)
            self.driver.find_element_by_xpath(".//*[@id=%s]"%(self.wd)).send_keys(Keys.ENTER)

            r= self.driver.find_element_by_xpath(".//*[@id='filterBlock']/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
            sleep(5)
            u= self.driver.find_elements_by_xpath(".//*[@id='controls-top']/div[4]/label/select/option")
            a=0
            for i in range(len(u)):
                if u[i].text == "Ratings":
                    a=i
            u[a].click()
            v= self.driver.find_element_by_xpath(".//*[@id='filterBlock']/div/div/div/div[2]/div[2]/ul/li[2]/a").click()

            sleep(5)

    def tear_down(self):
        self.driver.get_screenshot_as_png()
        self.driver.save_screenshot('screenshot.png')
        self.driver.close()

e=sel_exc()
e.enter_data()
e.tear_down()