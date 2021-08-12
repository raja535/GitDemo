from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Raja")
driver.find_element_by_css_selector("input[name='email']").send_keys("Raja.chinna.a5555@gmail.com")
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element_by_xpath("//input[@id='exampleInputPassword1']").send_keys("81424136")
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_css_selector("[class*='alert-success']").text
assert "Success" in message
#driver.close()