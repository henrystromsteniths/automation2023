from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'#open swappie.se website in chrome'
driver.get("https://swappie.com/se/?changeLang")
driver.fullscreen_window()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='declineAllConsentSummary']").click()
soki = driver.find_element(By.XPATH, '//*[@id="search"]')
soki.send_keys('920021025303')
soki.send_keys(Keys.ENTER)
time.sleep(4)

def test_kollamob():
    item1 = driver.find_element(By.XPATH, "//*[@id='campaign-collection-page']/div[2]/div[2]/a[6]/div[2]/div[1]/span")
    item1 = item1.text
    assert "iPhone 12 PRO" in item1

def test_kollaskick():
    item2 = driver.find_element(By.XPATH, "//*[@id='campaign-collection-page']/div[2]/div[2]/a[6]/div[2]/span/div/span[2]")
    item2 = item2.text
    assert "Utmärkt" in item2

def test_kollapris():
    item3 = driver.find_element(By.XPATH, "//*[@id='campaign-collection-page']/div[2]/div[2]/a[6]/div[2]/div[4]/span[1]")
    item3 = item3.text
    assert "8 369 kr" in item3


