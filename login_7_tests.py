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
import datetime
from datetime import date



class login_page(unittest.TestCase):
    def setUp(self):

        '''Fields of INIT'''
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.url = "https://qa-www.freeconferencecallhd.com/login"
        self.logo_link = "//a[@title='FreeConferenceCallHD.com']"
        self.wait = WebDriverWait(self.driver, 10)

        '''Static data'''
        self.email = "autotests@gmail.com"
        self.password = "pereriv123"

        '''Generators'''
        self.email_generator = str(random.randint(10000, 100000)) + '@mail.ru'
        self.pass_generator = random.randint(100000, 500000)

        '''Open dictionary'''
        with open('fields.json', 'r') as conf:
            self.fields = json.load(conf)

        '''Date of today'''
        today = date.today()  # 2017-05-03
        ### print(str(today.day) + "/" + str(today.month) + "/" + str(today.year))

    def test_LoginPage(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(self.url)

        ###Checking required fields###
        self.test_Required_Fields()
        print()

        ###Checking forgot links of password###
        self.test_ForgotPassLinks()
        print()

        ###Sending email for not existing account###
        self.test_SendingEmailNotExistingAccount()
        print()

        ###Sending email for existing account###
        self.test_SendingEmailExistingAccount()
        print()

        ###LogIn and Stay Logged###
        self.test_LogInAndStayLogged()



    def test_Required_Fields(self):
        print("Requier field tests: ")

        '''Requier fields, checking of requier fields'''
        try:
            self.driver.find_element(By.XPATH, self.fields["Login"]["Submit"]).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields["Login"]["Verif"])))
            print("PASSED: Checking of required fields is correct. Label of errors: " + self.driver.find_element(By.XPATH,self.fields["Login"]["Verif"]).text)
        except:
            print("FAILED: Checking of requier fields is incorrect")

        '''Incorrect value of fields'''
        try:
            self.driver.find_element(By.XPATH, self.fields["Login"]["Email"]).clear()
            self.driver.find_element(By.XPATH, self.fields["Login"]["Email"]).send_keys("gds@fg@@.ru")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields["Login"]["EmailError"])))
            print("PASSED: Checking of Email field is correct. Label of error: " + self.driver.find_element(By.XPATH,self.fields["Login"]["EmailError"]).text)
        except:
            print("FAILED: Field of Email works incorrect")

    def test_ForgotPassLinks(self):
        print("Checking forgot links of password: ")
        #forgot link
        #have account link
        try:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, self.fields["Login"]["ForgotPass"]).click()
            self.driver.save_screenshot("screens/login/forgot.png")
            self.driver.find_element(By.XPATH, self.fields["Login"]["HaveAcc"]).click()
            self.driver.save_screenshot("screens/login/haveacc.png")
            print("PASSED: Links work correct")
        except:
            print("FAILED: Forgot password and Have account links")

    def test_SendingEmailNotExistingAccount(self):
        print("Sending email for not existing account: ")
        try:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, self.fields["Login"]["ForgotPass"]).click()
            self.driver.find_element(By.XPATH, self.fields["Login"]["ForgotMail"]).send_keys(self.email_generator)
            self.driver.find_element(By.XPATH, self.fields["Login"]["SubmitForgot"]).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields["Login"]["NotExist"])))
            self.driver.save_screenshot("screens/login/notexistingmail.png")
            print("PASSED: " + self.driver.find_element(By.XPATH, self.fields["Login"]["NotExist"]).text)
        except:
            print("FAILED: Incorrect working of email field")

    def test_SendingEmailExistingAccount(self):
        print("Existing Email: ")
        try:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, self.fields["Login"]["ForgotPass"]).click()
            self.driver.find_element(By.XPATH, self.fields["Login"]["ForgotMail"]).clear()
            self.driver.find_element(By.XPATH, self.fields["Login"]["ForgotMail"]).send_keys(self.email)
            self.driver.find_element(By.XPATH, self.fields["Login"]["SubmitForgot"]).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields["Login"]["SentMail"])))
            self.driver.save_screenshot("screens/login/existingmail.png")
            print("PASSED: Message was sent.")
            print("!!!CHECK YOUR EMAIL!!!")
        except:
            print("FAILED: Message was not sent")

    def test_LogInAndStayLogged(self):
        print("LogIn test: ")
        try:
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, self.fields["Login"]["Email"]).clear()
            self.driver.find_element(By.XPATH, self.fields["Login"]["Email"]).send_keys(self.email)
            self.driver.find_element(By.XPATH, self.fields["Login"]["Pass"]).clear()
            self.driver.find_element(By.XPATH, self.fields["Login"]["Pass"]).send_keys(self.password)
            try:
                if self.driver.find_element(By.XPATH, self.fields["Login"]["Remember"]).is_selected():
                    pass
                else:
                    self.driver.find_element(By.XPATH, self.fields["Login"]["Remember"]).click()
                print("PASSED: Stay Logged In works correct")
            except:
                print("FAILED: Stay Logged In not clickable")

            self.driver.find_element(By.XPATH, self.fields["Login"]["Submit"]).click()
            self.driver.save_screenshot("screens/login/logingood.png")
            print("PASSED: You have been logged")
        except:
            print("FAILED: You have not been logged")

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()