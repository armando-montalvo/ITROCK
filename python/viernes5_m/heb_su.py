import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import sleep
from selenium.webdriver.support.ui import Select


class heb_su(object):

    def __init__(self):
        self.drive=webdriver.Firefox()
        self.drive.maximize_window()
        #self.drive.delete_all_cookies()
        self.book=xlrd.open_workbook('test.xls').sheet_by_index(0)
        self.search= ".//*[@id='search']"
        self.combo1= ".//*[@id='select-categories']/option"
        self.list_icon= ".//*[@id='top']/body/div[1]/div/div[4]/div/" \
                        "div[2]/div[2]/div[2]/div[1]/div[2]/p[1]/a"
        self.combo2= ".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]" \
                     "/div[2]/div[2]/div[1]/div[2]/div[1]/div/select/option"
        self.quantity= ".//*[@id='qty-420517']"
        self.close= ".//*[@id='closeBtn']"
        self.comprar= ".//*[@id='addcart-listmode']"
        self.subitem= ".//*[@id='products-list']/li[4]/div[2]/div/div[2]/h2/a"
        self.comprar= ".//*[@id='addcart-listmode']"
        self.inc= "//*[@id='plus-420517']"


    def enter(self):
        self.drive.delete_all_cookies()
        self.drive.get("http://www.heb.com.mx/")
        self.drive.find_element_by_xpath(".//*[@id='hs-eu-confirmation-button']").click()
        adv=  self.drive.find_element_by_xpath(".//*[@id='top']/body/div[2]/div/"
                                               "div[5]/div/div/div[1]/h1").text
        assert 'Recomendación de la semana' == adv
        reco= self.drive.find_element_by_xpath(".//*[@id='top']/body/div[2]/div/"
                                               "div[5]/div/div/div[2]/div[1]/h2[1]").text
        print(adv+': '+reco)


    def buy(self,v):
        list=self.book.row(v+1)
        srch_opt=self.drive.find_elements_by_xpath(self.combo1)

        for j in srch_opt:
            if j.text == list[0].value:
                j.click()

        self.drive.find_element_by_xpath(self.search).send_keys(list[1].value)
        self.drive.find_element_by_xpath(self.search).send_keys(Keys.ENTER)
        self.drive.implicitly_wait(10)
        self.drive.find_element_by_xpath(self.list_icon).click()
        cmb=self.drive.find_elements_by_xpath(self.combo2)

        for z in cmb:
            if 'Precio' in z.text:
                z.click()
                break

        elements= self.drive.find_elements_by_css_selector(".item")
        elen=len(elements)
        var=0
        for i,w in enumerate(elements):
            if list[3].value in w.text:
                print("The search '%s' is in the product '%s'"%(list[1].value, list[3].value))
                var=i

        print(var,len(elements))
        incb=self.drive.find_elements_by_css_selector(".qty")
        cp = self.drive.find_elements_by_css_selector("#addcart-listmode")

        for n,m in enumerate(incb):
            if n == var:
                m.clear()
                m.send_keys(int(list[2].value))
                cp[n].click()

        sleep(5)
        if v==0:
            self.drive.find_element_by_xpath(".//*[@id='closeBtn']").click()
            u = self.drive.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/"
                                                 "div[4]/div/div[2]/div[2]/ul[2]/li/ul/li/span")
            assert 'se agregó al carrito' in u.text
            numy = int(self.drive.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[3]").text)
            self.drive.find_element_by_xpath(".//*[@id='gotocar']/div/a").send_keys(Keys.ENTER)
            price = self.drive.find_element_by_xpath(".//*[@id='cart-sidebar']/li"
                                                     "/div/table[1]/tbody/tr/td/span").text
            price = float(price[2:].replace(",", ""))
            print("The total charge is %f" % (price * numy))
            self.drive.find_element_by_xpath(".//*[@id='btnMinicart']").click()
        else:
            self.drive.find_element_by_xpath(".//*[@id='sbmStoreSelect']").click()
            sleep(4)
            numy = int(self.drive.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[3]").text)
            print('The actual number of items in the car is: ',numy)
            self.drive.save_screenshot('sshot.png')

        #cp=self.drive.find_elements_by_css_selector("#addcart-listmode")[var].click()


r=heb_su()
for i in range(2):
    r.enter()
    r.buy(i)