
import pytest

from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities import XLutils
from utilities.ReadConfig import ReadConfigClass
from utilities.Logger import log_generator_class


@pytest.mark.usefixtures("driver_setup")
class Test_User_Login_Excel_DDT_Class_002:

    login_url = ReadConfigClass.get_login_url()
    # Initializing the logger, called loggen_method from loggenerator class in utitlties folder
    log = log_generator_class.loggen_method()
    # Initializing the driver
    driver = None

    #Excel_File_Path = ".\\TestData\\Test_Data.xlsx"
    Excel_File_Path = r'C:\PycharmBasic\folder\Credkart_login_testcases\TestData\Test_Data.xlsx'


    #
    # @pytest.mark.regression
    # @pytest.mark.group1
    # @pytest.mark.flaky(reruns=0, reruns_delay=2)
    def test_CredKart_User_Login_Excel_DDT_004(self):
        self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is started")
        """Test verify_user_login method with valid credentials."""
        self.log.info("Opening Browser")
        self.lp = Login_Page_Class(self.driver)
        self.driver.get(self.login_url)
        self.log.info(f"Going to CredKart URL ->{self.login_url}")
        # Read data from Excel
        self.log.info("Reading data from Excel")
        self.log.info("Reading the number of rows from Excel")
        excel_row_count = XLutils.RowCount(self.Excel_File_Path, "CredKart_login_Data")
        print(f"Number of rows in Excel is :  {excel_row_count}")
        self.log.info(f"Number of rows in Excel is :  {excel_row_count}")
        # Result_List=[]
        for i in range(2, excel_row_count + 1):
            self.log.info(f"Reading data from row number : {i} in excel")
            self.email = XLutils.ReadData(self.Excel_File_Path, "CredKart_login_Data", i, 1)
            self.password = XLutils.ReadData(self.Excel_File_Path, "CredKart_login_Data", i, 2)
            self.expected_result = XLutils.ReadData(self.Excel_File_Path, "CredKart_login_Data", i, 3)

            self.log.info(f"Entering email :{self.email}")
            self.lp.Enter_Email(self.email)
            self.log.info(f"Entering password :{self.password}")
            self.lp.Enter_Password(self.password)
            self.log.info("Clicking Login button")
            self.lp.Click_submit_Button()
            self.log.info("Verify User is logged in or not")
            if self.lp.verify_user_Login_or_registration() == "pass":
                actual_result = "login_pass"
                self.log.info(f"User '{self.email}' is  logged in and actual result is : {actual_result}")
                self.log.info("Taking Screenshot for Pass")
                self.driver.save_screenshot(f".\\Screenshots\\test_CredKart_User_Login_Excel_DDT_004_{self.email}_pass.png")
            else:
                actual_result = "login_fail"
                self.log.info(f"User '{self.email}' is not logged in and actual result is : {actual_result}")
                self.log.info("Taking Screenshot for Fail")
                self.driver.save_screenshot(f".\\Screenshots\\test_CredKart_User_Login_Excel_DDT_004_{self.email}_fail.png")


            if self.expected_result == actual_result:
                test_case_status = "Pass"
            else:
                test_case_status = "Fail"

            XLutils.WriteData(self.Excel_File_Path, "CredKart_login_Data", i, 4, actual_result)
            XLutils.WriteData(self.Excel_File_Path, "CredKart_login_Data", i, 5, test_case_status)
            # Result_List.append(test_case_status)
            self.driver.get(self.login_url)

        # if "Fail" in Result_List:
        #     self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is failed")
        #     self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is completed\n")
        #     assert False
        # else:
        #     self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is Pass")
        #     self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is completed\n")





"pytest -v -n auto --html=HtmlReports/my_report.html --browser chrome"
