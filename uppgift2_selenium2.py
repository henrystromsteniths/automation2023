from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'#open swappie.se website in chrome'
driver.get("https://swappie.com/se/jul")
driver.fullscreen_window()
time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='declineAllConsentSummary']").click()
# soki = driver.find_element(By.XPATH, '//*[@id="search"]')
# soki.send_keys('iPhone 12 Pro')
# soki.send_keys(Keys.ENTER)
# time.sleep(4)

def test_kollamob():
    item1 = driver.find_element(By.XPATH, "//*[@id='campaign-collection-page']/div[2]/div[2]/a[6]/div[2]/div[1]/span")
    item1 = item1.text
    assert "iPhone 12 Pro" in item1



