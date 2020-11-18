from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')  # 不要出现浏览器实体

# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://mofanpy.com/")
driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"数据处理 ▾").click()
driver.find_element_by_link_text(u"网页爬虫").click()

# get html
html = driver.page_source
driver.get_screenshot_as_file('./img/screenshot2.png')
time.sleep(2)
driver.close()
print(html[:200])
