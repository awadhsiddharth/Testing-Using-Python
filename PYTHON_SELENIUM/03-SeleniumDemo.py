# pip install selenium
# Web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.co.in/?gws_rd=ssl")

textBox = driver.find_element(By.NAME, "q")
textBox.send_keys("Vladimir Putin")
textBox.send_keys(Keys.ENTER)

# driver.close()