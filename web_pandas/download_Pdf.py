from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://github.com/iCSToCS/CSBook')

print(link)

# time.sleep(10)

# passwd = driver.find_elements_by_xpath('/html/body/div[4]/div/main/div[3]/div/div/div[2]/div[1]/div[3]/div[2]/article/ul[2]/li[1]/text()[2]')
# driver.find_elements_by_xpath('/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/article/ul[2]/li[1]/a')[0].click()


# print(passwd)