from selenium import webdriver # Selenium must be installed ( pip install selenium )

driver = webdriver.Chrome() # Uses chrome as your browser
driver.get("https://driverpracticaltest.direct.gov.uk/login")

licence_number = driver.find_element_by_name("username")
licence_number.send_keys("YOUR LICENCE NUMBER HERE")

ref_number = driver.find_element_by_name("password")
ref_number.send_keys("YOUR BOOKING REFERENCE NUMBER HERE")

submit = driver.find_element_by_name("booking-login")
submit.click()

change_date = driver.find_element_by_id("date-time-change")
change_date.click()

search = driver.find_element_by_id("driving-licence-submit")
search.click()


