import pytest
from selenium.webdriver.common.by import By

from pageObjects.CheckOut_Page import CheckOut_class
from utilities.Logger import log_generator_class
from utilities.ReadConfig import ReadConfigClass
from utilities.additional_utilities import additional_utilities_class


@pytest.mark.usefixtures("driver_setup")
class Test_CredKart_CheckOut_006:
    # Reading the data from the config file
    email = ReadConfigClass.geta_data_for_email()
    password = ReadConfigClass.geta_data_for_password()
    login_url = ReadConfigClass.get_login_url()
    homepage_url = ReadConfigClass.get_homepage_url()
    registration_url = ReadConfigClass.get_register_url()

    key1 = ReadConfigClass.section1_data()

    # Initializing the logger, called loggen_method from loggenerator class in utitlties folder
    log = log_generator_class.loggen_method()
    driver = None

    @pytest.mark.sanity
    @pytest.mark.dependency(name="test_CredKart_User_Profile_001::Test_User_Profile_Class_001::test_verify_CredKart_Url_001")
    def test_CheckOut_008(self):
        self.cc = CheckOut_class(self.driver)
        self.log.info("Testcase test_CheckOut_008 is started")
        """Test verify_user_login method with valid credentials."""
        self.log.info("Opening Browser")
        self.driver.maximize_window()
        self.driver.get(self.login_url)
        self.log.info(f"Going to CredKart URL ->{self.login_url}")
        self.log.info(f"Entering email :{self.email}")
        additional_utilities_class.explicit_wait(self.driver, (By.ID, self.cc.text_email_id), 10)
        self.cc.Enter_Email(self.email)
        self.log.info(f"Entering password :{self.password}")
        self.cc.Enter_Password(self.password)
        self.log.info("Clicking Login button")
        self.cc.Click_submit_Button()
        self.log.info("Click on Mac book pro")
        self.log.info("Click on add to cart")
        self.log.info("Click on proceed to checkout")
        self.cc.Click_macbookpro()
        self.log.info(" Enter First name")
        self.cc.Enter_Firstname("Credence")
        self.log.info(" Enter Last name")
        self.cc.Enter_Lastname("Credence")
        self.log.info(" Enter Phone")
        self.cc.Enter_Phone("1234567890")
        self.log.info(" Enter Address")
        self.cc.Enter_Address("Pune, Maharashtra, India, Earth")
        self.log.info(" Enter Zipcode")
        self.cc.Enter_Zipcode("411413")
        self.log.info(" Select State")
        self.cc.Select_State("Delhi")
        self.log.info(" Enter Owner")
        self.cc.Enter_Owner("Credence")
        self.log.info(" Enter CVV")
        self.cc.Enter_CVV("043")
        self.log.info(" Enter Card Number")
        self.cc.Enter_CardNumber("5281")
        self.cc.Enter_CardNumber("0370")
        self.cc.Enter_CardNumber("4891")
        self.cc.Enter_CardNumber("6168")
        self.log.info(" Select Year")
        self.cc.Select_Year("2025")
        self.log.info(" Select Month")
        self.cc.Select_Month("May")
        self.log.info("Click on checkout")
        self.cc.Click_Checkout()
        self.log.info("Verifying success message")
        #additional_utilities_class.explicit_wait(self.driver, (By.XPATH, self.cc.success_message_xpath), 10)
        if self.cc.Verify_Success_Message() == "Your order has been placed successfully.":
            print(f"Order Number is : {self.cc.Get_Order_Number()}")
            additional_utilities_class.take_screenshot(self.driver, "test_CheckOut_008", "Pass")
            assert True
        else:
            additional_utilities_class.take_screenshot(self.driver, "test_CheckOut_008", "Pass")
            assert False
