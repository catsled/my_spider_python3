"""模拟qq空间登录"""

from selenium import webdriver

# 创建浏览器对象

driver = webdriver.Firefox()

# 请求qq空间网站
driver.get('https://www.qzone.com')

# 等待页面加载
driver.implicitly_wait(5)  # 等待5s

# 定位登录框
login_window = driver.find_element_by_xpath('//*[@id="login_frame"]')

# 进入框架
driver.switch_to.frame(login_window)

# 点击使用帐号密码登录
select = driver.find_element_by_xpath('//a[@id="switcher_plogin"]')
select.click()

# 获取用户名输入框并输入用户名
user_input = driver.find_element_by_xpath('//input[@id="u"]')
user_input.send_keys('12121212')

# 获取密码输入框并输入密码
password_input = driver.find_element_by_xpath('//input[@id="p"]')
password_input.send_keys('12346789')

# 点击登录
driver.implicitly_wait(3)
login_click = driver.find_element_by_xpath('//input[@id="login_button"]')
login_click.click()

driver.close()