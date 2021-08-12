from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()

radioButtons = driver.find_elements_by_name("radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected()

assert driver.find_element_by_name("show-hide").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_name("show-hide").is_displayed()
