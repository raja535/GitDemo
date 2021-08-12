import time

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(2)
Count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    time.sleep(2)
    button.click()


driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button[class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
promoMsg = driver.find_element_by_css_selector("span.promoInfo").text
assert promoMsg == "Code applied ..!"

