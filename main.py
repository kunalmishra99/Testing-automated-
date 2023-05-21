import sys

from selenium import webdriver;
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import Select
import time

options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://www.thesparksfoundationsingapore.org/")
print("\nLet's Check For The TestCases:\n")

# TestCase 1: Title
print("TestCase #1:")
if (driver.title):
    print("Title Verification Successful: ", driver.title)
else:
    print("Title Verification Failed!\n")

# TestCase 2: Home button
print("TestCase #2:")
try:
    driver.find_element("xpath","//a[@class='col-md-6 navbar-brand']").click()
    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

# TestCase 3: Check if navbar appears
print("TestCase #3:")
try:
    driver.find_element("xpath","//nav[@class='navbar navbar-default']")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

# TestCase 4: About Us Page
print("TestCase #4:")
try:
    driver.find_element("xpath","//a[normalize-space()='About Us']").click()
    time.sleep(3)
    driver.find_element("xpath","//ul[@class='dropdown-menu']//a[normalize-space()='Vision, Mission and Values']").click()
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

# TestCase 5: Policies and Code
print('TestCase #5:')
try:
    driver.find_element("xpath","//a[normalize-space()='Policies and Code']").click()
    time.sleep(3)
    driver.find_element("xpath","//ul[@class='dropdown-menu']//a[normalize-space()='Policies']").click()
    time.sleep(3)
    print('Policy page exists. Success!\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!\n')
    time.sleep(3)

# TestCase 6: Workshop page
print('TestCase #6:')
try:
    driver.find_element("xpath","//a[normalize-space()='Programs']").click()
    time.sleep(3)
    driver.find_element("xpath","//a[normalize-space()='Workshops']").click()
    time.sleep(3)
    driver.find_element("xpath","//a[@href='/programs/workshops/glimpses-for-kids-workshop/'][normalize-space()='Learn more']").click()
    time.sleep(3)
    print('Workshop Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 7: Links Page
print("TestCase #7")
try:
    driver.find_element("xpath","//a[normalize-space()='LINKS']").click()
    time.sleep(3)
    driver.find_element("xpath","//a[normalize-space()='Software & App']").click()
    time.sleep(3)
    driver.find_element("xpath","//div[@class='w3l_inner_section about-w3layouts']//li[3]").click()
    time.sleep(3)
    print('LINKS Verfication successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

# TestCase 8: Check the Footer
print('TestCase #8:')
try:
    driver.find_element("xpath","//a[normalize-space()='GRIP (Internship)']").click()
    print('Footer Works!\n')
    time.sleep(3)
except NoSuchElementException:
    print('Footer Does not work!\n')

# TestCase 9:   Check the Form
print("TestCase #9:")
try:
    driver.find_element("xpath","//a[normalize-space()='Join Us']").click()
    time.sleep(3)
    driver.find_element("xpath","//a[normalize-space()='Why Join Us']").click()
    time.sleep(3)
    driver.find_element("xpath","//input[@placeholder='Full Name']").send_keys('Ayrika')
    time.sleep(3)
    driver.find_element("xpath","//input[@placeholder='Email or Phone Number']").send_keys('ayrikachakrabarti@gmail.com')
    time.sleep(3)
    select = Select(driver.find_element("xpath","//select[@class='form-control']"))
    time.sleep(3)
    select.select_by_visible_text("Student")
    time.sleep(3)
    driver.find_element("xpath","//input[@value='Submit']").click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

# TestCase 10:   Check the Contact us Page
print("TestCase #10:")
try:
    driver.find_element("xpath","//a[normalize-space()='Contact Us']").click()
    time.sleep(3)
    info = driver.find_element("xpath","//p[normalize-space()='+65-8402-8590, info@thesparksfoundation.sg']")
    time.sleep(3)

    # print(info.text)
    if (info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')

    # assert driver.page_source.find("+65-8402-859, info@thesparksfoundation.sg")
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")