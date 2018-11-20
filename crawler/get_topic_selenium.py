from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/explore'
driver = webdriver.Chrome()
driver.get(url)

divs = driver.find_elements_by_xpath("//*[@id='js-explore-tab']/div[1]/div")

for link in divs:
    print(link)
    print(link.find_element_by_xpath('//h2/a').text)
