import unittest
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random


class Landing_Page(unittest.TestCase):
    def setUp(self):

        '''Fields of INIT'''
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.url = "https://qa-www.freeconferencecallhd.com/"
        self.logo_link = "//a[@title='FreeConferenceCallHD.com']"
        self.wait = WebDriverWait(self.driver, 10)

        '''Open dictionary'''
        with open('fields.json', 'r') as conf:
            self.fields = json.load(conf)
        # self.fields['NAME']['features']
        # '''Fields of TopBar'''
        # self.features = "//div[@class='navbar-collapse collapse']//a[@title='Features']"
        # self.support = "//div[@class='navbar-collapse collapse']//a[@title='Support']"
        # self.FAQ = "//div[@class='navbar-collapse collapse']//a[@title='FAQs']"
        # self.about_us = "//div[@class='navbar-collapse collapse']//a[@title='About Us']"
        # self.contact_us = "//div[@class='navbar-collapse collapse']//a[@title='Contact Us']"
        #
        # '''Fields of BottomBar'''
        # self.b_features = "//div[@class='footernav']//a[@title='Features']"
        # self.b_support = "//div[@class='footernav']//a[@title='Support']"
        # self.b_FAQ = "//div[@class='footernav']//a[@title='FAQs']"
        # self.b_about_us = "//div[@class='footernav']//a[@title='About Us']"
        # self.b_contact_us = "//div[@class='footernav']//a[@title='Contact Us']"
        #
        # '''Terms'''
        # self.terms = "//a[@id='termsofservice_link']"
        # self.close = "//button[@class='close']"
        #
        # '''Login button'''
        # self.LoginButton = "//a[@title='Log In']"
        #
        # '''Support number'''
        # self.support_num = "//span[@class='phone-number']"
        #
        # '''Fields of Sign Up'''
        # self.first_name = "//input[@name='first_name']"
        # self.last_name = "//input[@name='last_name']"
        # self.email = "//input[@name='email']"
        # self.password = "//input[@name='password']"
        # self.parsel_type = "//li[@class='parsley-type']"
        #
        '''Generators'''
        self.email_generator = str(random.randint(10000,100000))+ '@mail.ru'
        self.pass_generator = random.randint(100000,500000)
        #
        # '''Fields of HD Conferencing'''
        # self.hd_link = "//a[@title='HD Conferencing']"
        # self.setup_conf = "//a[@title='Setup Conference Call']"
        # self.set_conf = "//a[@title='Set Conference Preferences']"
        # self.get_call = "//a[@title='Get on the Call']"
        # self.after_call = "//a[@title='After the Call']"
        # self.back_to_top = "//a[@title='Back to top']"
        # self.web_based = "//a[@title='Web-Based Commands']"
        # self.phone_keypad = "//a[@title='Phone Keypad Commands']"
        # self.trouble_ticket = "//a[@title='Trouble Ticket']"
        # self.voip = "//a[@title='VoIP Dialer']"
        #
        # '''International'''
        # self.international_button = "//a[@title='International']"
        #
        # '''Web Controls'''
        # self.web_contrl_button = "//a[@title='Web Controls']"
        #
        # '''Store Field'''
        # self.appStore = "//a[@title='Download FreeConferenceCallhd.com mobile app for iOS on the App Store']"
        # self.googlePlay = "//a[@title='Download the FreeConferenceCallHD.com mobile app for Android on Google Play']"


    def test_LandingPageTest(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(self.url)

        ### LogIn test ###
        self.test_LogInButton()
        print()
        ### Support number test ###
        self.test_SupportNum()
        print()
        ### Top navigation test ###
        self.test_TopNav()
        print()
        ### Logo link test ###
        self.test_LogoLink()
        print()
        ### Bottom navigation test ###
        self.test_BottomNav()
        print()
        ### Terms test ###
        self.test_Terms()
        print()
        ### Negative Sign Up ###
        self.test_SignUpNegative()
        print()
        ### HD Links ###
        self.test_HDLink()
        print()
        ### International ###
        self.test_International()
        print()
        ### Web Controls ###
        self.test_WebControls()
        print()
        ### App Pages ###
        self.test_AppPages()
        print()
        ### About Us ###
        self.test_AboutUs()
        print()
        ### FAQ ###
        self.test_FAQ()


    def test_SupportNum(self):
        print("Support number test: ")
        try:
            number = self.driver.find_element(By.XPATH, self.fields['Support']['support_num'])
            print("PASSED: Support number: " + number.text)
        except:
            print("FAILED: Support number")

    def test_LogInButton(self):
        print("Login button test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['Login']['LoginButton']).click()
            try:
                self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields["Login"]["HeadText"])))
                self.driver.save_screenshot("screens/LandingPage/LoginPage.png")
            except:
                print("FAILED: Login page not found")
            self.driver.back()
            print("PASSED: Login button")
        except:
            print("FAILED: Login Button")

    def test_LogoLink(self):
        print("Logo link test: ")
        try:
            self.driver.find_element(By.XPATH, self.logo_link).click()
            print("PASSED: Logo link")
        except:
            print("FAILED: Logo link")

    def test_TopNav(self):
        print("Top navigation test: ")
        try:
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, self.fields['TopBar']['features']).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields['TopBar']['support']).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields['TopBar']['FAQ']).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields['TopBar']['about_us']).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields['TopBar']['contact_us']).click()
            print("PASSED: Top navigation")
        except:
            print("FAILED: Top navigation")

    def test_BottomNav(self):
        print("Bottom navigation test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['BottomBar']['b_features']).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields['BottomBar']['b_support']).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields['BottomBar']['b_FAQ']).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields['BottomBar']['b_about_us']).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields['BottomBar']['b_contact_us']).click()
            self.driver.back()
            self.driver.execute_script("window.scrollTo(0, 0)")
            print("PASSED: Bottom navigation")
        except:
            print("FAILED: Bottom navigation")

    def test_Terms(self):
        print("Terms test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['Terms']['terms']).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.fields['Terms']['close'])))
            self.driver.find_element(By.XPATH, self.fields['Terms']['close']).click()
            print("PASSED: Terms")
        except:
            print("FAILED: Terms")

    def test_SignUpNegative(self):
        print("Sign Up negative test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['SignUp']['first_name']).clear()
            self.driver.find_element(By.XPATH, self.fields['SignUp']['first_name']).send_keys("Antonio")
            self.driver.find_element(By.XPATH, self.fields['SignUp']['last_name']).clear()
            self.driver.find_element(By.XPATH, self.fields['SignUp']['last_name']).send_keys("Fernandos")
            self.driver.find_element(By.XPATH, self.fields['SignUp']['email']).clear()
            self.driver.find_element(By.XPATH, self.fields['SignUp']['email']).send_keys(self.pass_generator)
            self.driver.find_element(By.XPATH, self.fields['SignUp']['password']).clear()
            self.driver.find_element(By.XPATH, self.fields['SignUp']['password']).send_keys(self.email_generator)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fields['SignUp']['parsel_type'])))
            print(("PASSED: Negative Sign Up (" + "ERROR: " + self.driver.find_element(By.XPATH, self.fields['SignUp']['parsel_type']).text) + ")")
        except:
            print("FAILED: Negative Sign Up")

    def test_HDLink(self):
        print("Links of HD test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['HDConference']['hd_link']).click()
            self.driver.find_element(By.XPATH, self.fields['HDConference']['set_conf']).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.fields['HDConference']['set_conf']).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.fields['HDConference']['get_call']).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.fields['HDConference']['after_call']).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.fields['HDConference']['back_to_top']).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.fields['HDConference']['web_based']).click()
            self.driver.find_element(By.XPATH, self.fields['HDConference']['phone_keypad']).click()
            self.driver.find_element(By.XPATH, self.fields['HDConference']['trouble_ticket']).click()
            self.driver.find_element(By.XPATH, self.fields['HDConference']['voip']).click()
            self.driver.get(self.url)
            print("PASSED: HD Links")
        except:
            print("FAILED: HD Links")

    def test_International(self):
        print("International page test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['International']['international_button']).click()
            self.driver.save_screenshot("screens/LandingPage/international_page.png")
            self.driver.back()
            print("PASSED: International page")
        except:
            print("FAILED: International page")

    def test_WebControls(self):
        print("Web Control page test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['Controls']['web_control_button']).click()
            self.driver.save_screenshot("screens/LandingPage/WebControlsPage.png")
            self.driver.back()
            print("PASSED: Web Controls Page")
        except:
            print("FAILED: Web Controls Page")

    def test_AppPages(self):
        print("App pages test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['Store']['appStore']).click()
            time.sleep(5)
            hundles = self.driver.window_handles
            self.driver.switch_to.window(hundles[1])
            self.driver.save_screenshot("screens/LandingPage/appstore.png")
            self.driver.switch_to.window(hundles[0])
            self.driver.find_element(By.XPATH, self.fields['Store']['googlePlay']).click()
            hundles = self.driver.window_handles
            self.driver.switch_to.window(hundles[2])
            self.driver.save_screenshot("screens/LandingPage/playmarket.png")
            self.driver.switch_to.window(hundles[0])
            print("PASSED: App pages")
        except:
            print("FAILED: App pages")

    def test_AboutUs(self):
        print("About Us page test: ")
        try:
            self.driver.get(self.fields["Urls"]["about_us"])
            self.driver.save_screenshot("screens/LandingPage/map.png")
            self.driver.find_element(By.XPATH, self.fields["AboutUs"]["fcc_link"]).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields["AboutUs"]["fc_link"]).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields["AboutUs"]["hd_link"]).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields["AboutUs"]["sm_link"]).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields["AboutUs"]["smstudio_link"]).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.fields["AboutUs"]["fcc_inter_link"]).click()
            self.driver.back()
            print("PASSED: About Us")
        except:
            print("FAILED: About Us")

    def test_FAQ(self):
        print("FAQ test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields["TopBar"]["FAQ"]).click()
            self.driver.find_element(By.XPATH, self.fields["FAQ"]["General"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["FAQ"]["InterConf"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["FAQ"]["FeatureQ"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["FAQ"]["Setup"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["FAQ"]["Pricing"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["FAQ"]["Technical"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["FAQ"]["Back"]).click()
            self.driver.save_screenshot("faq.PNG")
            self.driver.back()
            print("PASSED: FAQ")
        except:
            print("FAILED: FAQ")

    def test_Support(self):
        print("Support page test: ")
        try:
            self.driver.find_element(By.XPATH, self.fields['TopBar']['support']).click()
            self.driver.find_element(By.XPATH, self.fields["Support"]["Setup"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["Support"]["SetCon"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["Support"]["Geton"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["Support"]["After"]).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.fields["Support"]["Back"]).click()
            time.sleep(1)
            ###
            self.driver.find_element(By.XPATH, self.fields["Support"]["Web"]).click()
            self.driver.find_element(By.XPATH, self.fields["Support"]["Phone"]).click()
            self.driver.find_element(By.XPATH, self.fields["Support"]["Trouble"]).click()
            self.driver.find_element(By.XPATH, self.fields["Support"]["VoIP"]).click()
            self.driver.find_element(By.XPATH, self.fields["Support"]["Logolink"]).click()
            print("PASSED: Support page")
        except:
            print("FAILED: Support page")

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()