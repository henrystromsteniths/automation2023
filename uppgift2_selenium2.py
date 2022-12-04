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


def test_kollamob():
    item1 = driver.find_element(By.XPATH, "//*[@id='campaign-collection-page']/div[2]/div[2]/a[6]/div[2]/div[1]/span")
    item1 = item1.text
    assert "iPhone 12 Pro" in item1

def test_kollaskick():
    item2 = driver.find_element(By.XPATH, "//*[@id='campaign-collection-page']/div[2]/div[2]/a[6]/div[2]/span/div/span[2]")
    item2 = item2.text
    assert "Utmärkt" in item2

def test_kollapris():
    item3 = driver.find_element(By.XPATH, "//*[@id='campaign-collection-page']/div[2]/div[2]/a[6]/div[2]/div[4]/span[1]")
    item3 = item3.text
    assert "8 369 kr" in item3

def test_intobasket1():
    driver.find_element(By.XPATH, "/html/body").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='main-area-section']/div[1]/div[2]/div[9]/button/span").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "// *[ @ id = 'tempered-glass-step-b'] / div[3] / div[2] / a").click()
    basket1 = driver.find_element(By.XPATH, "// *[ @ id = 'minicart-count']")
    basket1 = basket1.text
    assert basket1 == "1"










