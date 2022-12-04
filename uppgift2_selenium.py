from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'#open rexel website in chrome'
driver.get("https://www.rexel.se")
driver.fullscreen_window()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='declineAllConsentSummary']").click()
soki = driver.find_element(By.XPATH, '//*[@id="search"]')
soki.send_keys('920021025303')
soki.send_keys(Keys.ENTER)
time.sleep(4)

def test_kollaid():
    item1 = driver.find_element(By.XPATH, "//*[@id='pdp-content-slot-1']/div[1]/div[7]/div[5]/div/div[4]/div/div[2]")
    item1 = item1.text
    assert "920021025303" in item1

def test_kollaart():
    item2 = driver.find_element(By.XPATH, "//*[@id='pdp-content-slot-1']/div[1]/div[7]/div[5]/div/div[3]/div/div[2]")
    item2 = item2.text
    assert "8340186" in item2


def test_intobasket1():
    driver.find_element(By.XPATH, "//*[@id='addToCartDiv_8340186']/span").click()
    time.sleep(2)
    basket1 = driver.find_element(By.XPATH, "//*[@id='miniCartContainer']/span")
    basket1 = basket1.text
    assert basket1 == "1"



