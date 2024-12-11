import time

import faker
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities.ReadConfig import ReadConfigClass
from utilities.Logger import log_generator_class


@pytest.mark.usefixtures("driver_setup")
class Test_User_Login_Params_Class_003:
    # Reading the data from the config file
    login_url = ReadConfigClass.get_login_url()

    # Initializing the logger, called loggen_method from loggenerator class in utitlties folder
    log = log_generator_class.loggen_method()
    # Initializing the driver
    driver = None


    # @pytest.mark.sanity
    # @pytest.mark.group1
    # @pytest.mark.flaky(reruns=0, reruns_delay=2)

    def test_CredKart_User_Login_params_DDT_005(self, get_data_Credkart_login):
        self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is started")
        """Test verify_user_login method with valid credentials."""
        self.log.info("Opening Browser")
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.login_url)
        self.log.info(f"Going to CredKart URL ->{self.login_url}")

        self.email = get_data_Credkart_login[0]
        self.password = get_data_Credkart_login[1]
        self.expected_result = get_data_Credkart_login[2]

        self.log.info(f"Entering email :{self.email}")
        self.lp.Enter_Email(self.email)
        self.log.info(f"Entering password :{self.password}")
        self.lp.Enter_Password(self.password)
        self.log.info("Clicking Login button")
        self.lp.Click_submit_Button()
        self.log.info("Verify User is logged in or not")
        if self.lp.verify_user_Login_or_registration() == "pass":
            print("User is logged in")
            self.log.info("Taking Screenshot for Pass")
            self.driver.save_screenshot(f".\\Screenshots\\test_CredKart_User_Login_params_DDT_005_{self.email}_{self.password}_Pass.png")
            actual_result = "login_pass"
        else:
            self.log.info("Taking Screenshot for Fail")
            self.driver.save_screenshot(f".\\Screenshots\\test_CredKart_User_Login_params_DDT_005_{self.email}_{self.password}_Fail.png")
            print("User is not logged in")
            actual_result = "login_fail"

        if self.expected_result == actual_result:
            self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is Pass")
            self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is Completed\n")
            assert True
        else:
            self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is Fail")
            self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is Completed\n")
            assert False





"pytest -v -n auto --html=HtmlReports/my_report.html --browser chrome"

