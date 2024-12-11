import time

import faker
import pytest
from pytest_cov.embed import cleanup_on_signal
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities.ReadConfig import ReadConfigClass
from utilities.Logger import log_generator_class
from utilities.additional_utilities import additional_utilities_class, TestCase_Status

@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class_001:
    email = ReadConfigClass.geta_data_for_email()
    password = ReadConfigClass.geta_data_for_password()
    login_url = ReadConfigClass.get_login_url()
    homepage_url = ReadConfigClass.get_homepage_url()
    registration_url = ReadConfigClass.get_register_url()

    key1 = ReadConfigClass.section1_data()

    # Initializing the logger, called loggen_method from loggenerator class in utitlties folder
    log = log_generator_class.loggen_method()
    # Initializing the driver
    driver = None
    """Test cases for the UserProfile class."""
    @pytest.mark.sanity
    @pytest.mark.group1
    # @pytest.mark.flaky(max_runs=3)
    def test_verify_CredKart_Url_001(self):

        self.log.info("Testcase test_verify_CredKart_Url_001 is started")
        self.driver.get(self.homepage_url)
        self.log.info("Opening Browser")
        self.log.info(f"Going to CredKart URL ->{self.homepage_url}")
        self.log.info("Checking Page Title")
        if self.driver.title == "CredKart":
            TestCaseStatus = "Pass"
            TestCase_Status.set_status("test_verify_CredKart_Url_001", True)
            print(TestCase_Status.get_status("test_verify_CredKart_Url_001"))
            self.log.info(f"Page Title:'{self.driver.title}' is  matches with expected title")
            #print("Test passed: Title matches with expected title")
            self.log.info("Taking Screenshot")
            #self.driver.save_screenshot(".\\Screenshots\\test_verify_CredKart_Url_001_pass.png")
            additional_utilities_class.take_screenshot(self.driver,"test_verify_CredKart_Url_001", "Pass" )
            self.log.info("Testcase test_verify_CredKart_Url_001 is passed")
            self.log.info("Testcase test_verify_CredKart_Url_001 is completed\n")
            assert True
        else:
            TestCase_Status.set_status("test_verify_CredKart_Url_001", False)
            print(TestCase_Status.get_status("test_verify_CredKart_Url_001"))
            self.log.info("Taking Screenshot")
            #self.driver.save_screenshot(".\\Screenshots\\test_verify_CredKart_Url_001_fail.png")
            additional_utilities_class.take_screenshot(self.driver, "test_verify_CredKart_Url_001", "Fail")
            self.log.info("Testcase test_verify_CredKart_Url_001 is failed")
            self.log.info("Testcase test_verify_CredKart_Url_001 is completed\n")
            assert False

    @pytest.mark.sanity
    @pytest.mark.group1
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    # @pytest.mark.skipif(not TestCase_Status.get_status("test_verify_CredKart_Url_001"), reason="test_verify_CredKart_Url_001 is failed")
    def test_CredKart_User_Login_002(self):
        self.log.info("Testcase test_CredKart_User_Login_002 is started")
        """Test verify_user_login method with valid credentials."""
        self.log.info("Opening Browser")
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.login_url)
        self.log.info(f"Going to CredKart URL ->{self.login_url}")
        self.log.info(f"Entering email :{self.email}")
        additional_utilities_class.explicit_wait(self.driver, (By.ID, self.lp.text_email_id), 10)
        self.lp.Enter_Email(self.email)
        self.log.info(f"Entering password :{self.password}")
        self.lp.Enter_Password(self.password)
        self.log.info("Clicking Login button")
        self.lp.Click_submit_Button()
        self.log.info("Verify User is logged in or not")
        if self.lp.verify_user_Login_or_registration() == "pass":
            print("User is logged in")
            self.log.info("Taking Screenshot for Pass")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_pass.png")
            self.log.info("Testcase test_CredKart_User_Login_002 is Pass")
            self.log.info("Testcase test_CredKart_User_Login_002 is Completed\n")
            assert True
        else:
            self.log.info("Taking Screenshot for Fail")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_fail.png")
            print("User is not logged in")
            self.log.info("Testcase test_CredKart_User_Login_002 is Fail")
            self.log.info("Testcase test_CredKart_User_Login_002 is Completed\n")
            assert False



    @pytest.mark.sanity
    @pytest.mark.group1
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    # @pytest.mark.skipif(not TestCase_Status.get_status("test_verify_CredKart_Url_001"),
    #                     reason="test_verify_CredKart_Url_001 is failed"
    #                     )
    def test_CredKart_User_Registration_003(self, faker):
        """Test verify_user_login method with valid credentials."""
        #self.driver = driver_setup
        self.log.info("Define the logs for this testcase :  Your Task")
        self.rp = Registration_Page_Class(self.driver)
        self.driver.get(self.registration_url)
        random_name = faker.name()
        print(f"randomname : {random_name}")
        random_email = faker.email()
        print(f"random_email : {random_email}")
        random_password = faker.password()
        print(f"random_password : {random_password}")
        # Enter the Name
        self.rp.Enter_Name(random_name)
        # Enter the Email
        self.rp.Enter_Email(random_email)
        # Enter the Password
        self.rp.Enter_Password(random_password)
        # Enter the Confirm Password
        self.rp.Enter_Confirm_Password(random_password)
        # Click the register button
        self.rp.Click_submit_Button()
        if self.rp.verify_user_Login_or_registration() == "pass":
            print("User is registered")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Registration_003_pass.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Registration_003_fail.png")
            print("User is not registered")
            assert False


"pytest -v -n auto --html=HtmlReports/my_report.html --browser chrome"

# robot
# bdd
# api automation
# database automation
#web automation --> syllabus
# uipath
# tosca
# work fusion

