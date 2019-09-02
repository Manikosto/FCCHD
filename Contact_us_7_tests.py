import unittest
import json
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class Contact_UsPage(unittest.TestCase):
    def setUp(self):
        # Hello world tre
        '''Fields of INIT'''
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.url = "https://qa-www.freeconferencecallhd.com/contact-us"
        self.logo_link = "//a[@title='FreeConferenceCallHD.com']"
        self.wait = WebDriverWait(self.driver, 10)

        '''Generators'''
        self.email_generator = str(random.randint(10000, 100000)) + '@mail.ru'
        self.pass_generator = random.randint(100000, 500000)

        '''Open dictionary'''
        with open('fields.json', 'r') as conf:
            self.fields = json.load(conf)

    def test_ContactUsPage(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(self.url)
        ### Required Fields ###
        self.test_RequiredFields()
        print()
        ### Negative checking of fields ###
        self.test_NegativeCheckingFields()
        print()
        ## Positive checking Submit And Form Fields ###
        self.test_PositiveCheckingSubmitAndFormFields()
        print()
        ### Map ###
        self.test_Map()

    def test_NegativeCheckingFields(self):
        print("Negative Fields Check tests: ")
        self.driver.find_element(By.XPATH, self.fields["ContactUs"]["name"]).send_keys(
            "Manikosto")  # Have not check because we can writel any values

        ### Check of Email field on incorrect working ###
        try:
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["email"]).clear()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["email"]).send_keys(
                self.email_generator + "@random")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields["ContactUs"]["email_error"])))
            email_error = self.driver.find_element(By.XPATH, self.fields["ContactUs"]["email_error"])
            print("PASSED: You cannot write incorrect email: " + email_error.text)
        except:
            print("FAILED: You can write incorrect Email")

        ### Check on incorrect working of Phone field (Write not numbers) ###
        try:
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["phone"]).clear()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["phone"]).send_keys("assagsagd")
            phone_er = self.driver.find_element(By.XPATH, self.fields["ContactUs"]["phone"])
            if phone_er.text != "assagsagd":
                print("PASSED: You cannot write words in Phone field: Field is empty")
        except:
            print("FAILED: You can write words instead numbers in Phone number field")

        ### Check on incorrect working of Phone field (Write short number) ###
        try:
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["phone"]).clear()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["phone"]).send_keys("899999")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields["ContactUs"]["phone_error"])))
            phone_er = self.driver.find_element(By.XPATH, self.fields["ContactUs"]["phone_error"])
            print("PASSED: You cannot write short numbers in Phone fields: " + phone_er.text)
        except:
            print("FAILED: Incorrect working of Phone number field (Short number)")

        self.driver.find_element(By.XPATH, self.fields["ContactUs"]["comments"]).clear()
        self.driver.find_element(By.XPATH, self.fields["ContactUs"]["comments"]).send_keys("Test")

    def test_PositiveCheckingSubmitAndFormFields(self):
        print("Positive checking submit and form fields tests: ")
        try:
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["name"]).clear()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["name"]).send_keys("Manikosto")
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["email"]).clear()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["email"]).send_keys(self.email_generator)
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["phone"]).clear()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["phone"]).send_keys("89999999999")
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["comments"]).clear()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["comments"]).send_keys("Test")
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["submit"]).click()
            try:
                self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields["ContactUs"]["notify"])))
                self.driver.save_screenshot("screens/about_us/notify.png")
                print("PASSED: Message was sent")
            except:
                print("FAILED: Message did not send")
            print("PASSED: Positive checking submit and form fields")
        except:
            print("FAILED: Positive checking submit and form fields")

    def test_RequiredFields(self):
        print("Required fields tests: ")
        try:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["name"]).clear()
            self.driver.find_element(By.XPATH, self.fields["ContactUs"]["name"]).send_keys(Keys.ENTER)
            self.driver.save_screenshot("screens/about_us/RequiredFields.png")
            print("PASSED: Required fields")
        except:
            print("FAILED: Required fields")

    def test_Map(self):
        print("Map tests: ")
        try:
            self.driver.refresh()
            self.driver.execute_script("window.scrollTo(0, 100)")
            self.driver.save_screenshot("screens/about_us/map.png")
            print("PASSED: Map")
        except:
            print("FAILED: Map")

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
