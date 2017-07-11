from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

# navigate to the application home page
driver.get("http://www.liverpool.com.mx/tienda/browse/store.jsp")

# get the search textbox
search_field = driver.find_element_by_xpath(".//*[@id='inAlmacen']").send_keys('Guadalajara')
driver.find_element_by_xpath(".//*[@id='inAlmacen']").send_keys(Keys.ENTER)

sleep(5)

ls= driver.find_elements_by_xpath(".//*[@id='lstAlmacenes']/option")
a=0
for i in range(len(ls)):
    if ls[i].text == "Fábricas de Francia Guadalajara Centro":
        ls[i].click()
        a=i

print(ls[a].text)