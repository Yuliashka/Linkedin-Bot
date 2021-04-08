# LINK FOR JOB: https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103350119&keywords=junior%20python%20developer&location=Italy

from selenium import webdriver
import time

# PATH TO CHROME DRIVER:
chrom_driver_path = "C:\Development\chromedriver.exe"

# SHOWING A PATH TO OUR DRIVER:
driver = webdriver.Chrome(executable_path=chrom_driver_path)

# GETTING AND OPENNING THE PAGE:
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=1569416603&f_T=25169&geoId=103350119&keywords=python%20developer&location=%D0%98%D1%82%D0%B0%D0%BB%D0%B8%D1%8F&sortBy=R")

# GETTING THE LOGIN BUTTON:
time.sleep(4)
login_button = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")

# CLICKING THE LOGIN BUTTON:
login_button.click()

time.sleep(2)

# FILLING IN LOGIN FORM:
email = driver.find_element_by_name("session_key")
email.send_keys("your mail")

time.sleep(2)
password = driver.find_element_by_name("session_password")
password.send_keys("your password")

time.sleep(2)
enter_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
enter_button.click()


# CLICKING APPLY BUTTON:
time.sleep(5)
apply_button = driver.find_element_by_class_name("jobs-save-button")
apply_button.click()

time.sleep(5)
link = driver.find_element_by_link_text("См. сохраненные вакансии")
time.sleep(8)
link.click()



