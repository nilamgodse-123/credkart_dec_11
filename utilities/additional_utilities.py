# take screenshot
# explicit wait
# dependency --> title--> dont got to login skip
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class additional_utilities_class:
    @staticmethod
    def take_screenshot(driver, testcase_name, status):
        return driver.save_screenshot(f".\\Screenshots\\{testcase_name}_{status}.png")


    @staticmethod
    def explicit_wait(driver, element, time_for_wait=5):
        try:
            WebDriverWait(driver, time_for_wait).until(expected_conditions.visibility_of_element_located(element))
        except :
            pass


class TestCase_Status:
    status={}
    @staticmethod
    def set_status(testcase_name,status):
        TestCase_Status.status[testcase_name]=status

    @staticmethod
    def get_status(testcase_name):
        return TestCase_Status.status.get(testcase_name)