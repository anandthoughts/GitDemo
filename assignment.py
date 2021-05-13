import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

list1 = ["Mushroom - 1 Kg", "Cashews - 1 Kg"]
list2 = []

driver.find_element_by_xpath("//input[@type='search']").send_keys("sh")
time.sleep(2)
driver.find_elements_by_css_selector("div[class='product']")

search = driver.find_elements_by_css_selector("h4[class*='product-name']")
for sch in search:
    list2.append(sch.text)
print(list2)

assert list1 == list2



