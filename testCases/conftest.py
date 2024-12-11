import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("launching chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("launching firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("launching edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("chrome headless browser started")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no visible browser windows)
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("chrome headless browser started")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no visible browser windows)
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # attaching driver to class
    request.cls.driver = driver
    yield driver # driver is return to the test cases or method
    driver.quit()
    print("Browser closed")


def pytest_metadata(metadata):
    metadata["Class"] = "Credence_Test#20"
    metadata["Description"] = "Test to verify the Credence homepage and search functionality"
    metadata["Test Type"] = "Functional"
    metadata["Author"] = "Credence : Test Automation Team"
    metadata["URL"] = "https://automation.credence.in/" # to add url key in report
    metadata.pop("Platform", None) # to remove the platform key
    # metadata.pop("Plugins", None)
    # How to edit summary in html report is your task



@pytest.fixture(params=[
    ("Credencetest@test.com", "Credence@123", "login_pass"),
    ("Credencetest@test.com1", "Credence@123", "login_fail"),
    ("Credencetest@test.com", "Credence@1231", "login_fail"),
    ("Credencetest@test.com1", "Credence@1231", "login_fail"),
("Credencetest@test.com1", "Credence@1231", "login_fail")
])
def get_data_Credkart_login(request):
    return request.param


from pageObjects.Login_Page import Login_Page_Class
@pytest.fixture
def login_fixture(driver_setup):
    driver = driver_setup
    lp= Login_Page_Class(driver)
    driver.get("https://automation.credence.in/login")
    driver.implicitly_wait(10)
    lp.Enter_Email("Credencetest@test.com")
    lp.Enter_Password("Credence@123")
    lp.Click_submit_Button()

    return driver