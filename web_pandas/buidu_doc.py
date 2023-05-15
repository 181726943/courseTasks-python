from selenium import webdriver
import time
import re
#driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver = webdriver.Chrome()

# # 模拟爱奇艺登录
# driver.get('https://vip.iqiyi.com/?fv=zz_57b2d4c27f403-136358819-224842')
# # 调用立即登录的js代码
# # js = 'document.getElementsByClassName("vip_login-btn")[0].click();'
# # driver.execute_script(js)

# time.sleep(5)
# # 模拟点击登录
# login = driver.find_elements_by_class_name("vip_login-btn")[0]
# login.click()
# time.sleep(5)


# # 模拟百度搜索
# driver.get('http://www.baidu.com/')
# driver.find_element_by_id("kw").send_keys("github")  #搜说github
# driver.find_element_by_id("su").click()
# time.sleep(5)
# # 进入GitHub
# driver.find_element_by_class_name("t").click()

# js = 'document.getElementsByClassName("s-top-login-btn c-btn c-btn-primary c-btn-mini lb")[0].click();'
# driver.execute_script(js)



