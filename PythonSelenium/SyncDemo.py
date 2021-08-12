import time

from selenium import webdriver
import time
cartList1 = []
cartList2 = []
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(2)
Count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    time.sleep(2)
    cartList1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(cartList1)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
veggies = driver.find_elements_by_css_selector("p.product-name")
for veggie in veggies:
    cartList2.append(veggie.text)
print(cartList2)
assert cartList1 == cartList2
originalAmount = driver.find_element_by_class_name("discountAmt").text
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button[class='promoBtn']").click()
promoMsg = driver.find_element_by_css_selector("span[class='promoInfo']").text
assert promoMsg == "Code applied ..!"
discountedAmount = driver.find_element_by_class_name("discountAmt").text
assert float(discountedAmount) < int(originalAmount)
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
totalAmt = 0
for amount in amounts:
    totalAmt = totalAmt + int(amount.text)
print(totalAmt)
assert totalAmt == int(driver.find_element_by_class_name("totAmt").text)
