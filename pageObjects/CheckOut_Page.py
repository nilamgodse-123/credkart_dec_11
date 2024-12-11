from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.Login_Page import Login_Page_Class


class CheckOut_class(Login_Page_Class):

    click_macbookpro_xpath = "//h3[normalize-space()='Apple Macbook Pro']"
    click_addtocart_xpath = "//input[@value='Add to Cart']"
    click_proceedtocheckout_xpath = "//a[normalize-space()='Proceed to Checkout']"
    text_Firstname_xpath = "//input[@id='first_name']"
    text_lastname_xpath = "//input[@id='last_name']"
    text_phone_xpath = "//input[@id='phone']"
    text_address_xpath = "//textarea[@id='address']"
    text_zipcode_xpath = "//input[@id='zip']"
    dropdown_state_xpath = "//select[@id='state']"
    text_owner_xpath = "//input[@id='owner']"
    text_cvv_xpath = "//input[@id='cvv']"
    text_CardNumber_xpath = "//input[@id='cardNumber']"
    dropdown_year_xpath = "//select[@id='exp_year']"
    dropdown_month_xpath = "//select[@id='exp_month']"
    click_checkout_xpath = "//button[@id='confirm-purchase']"
    success_message_xpath = "//p[@class='lead w-lg-50 mx-auto']"
    Order_number_css = "body > div:nth-child(2) > div:nth-child(1) > p:nth-child(3) > a:nth-child(1)"


    def __init__(self, driver):
        self.driver = driver


    def Click_macbookpro(self):
        self.driver.find_element(By.XPATH, self.click_macbookpro_xpath).click()
        self.driver.find_element(By.XPATH, self.click_addtocart_xpath).click()
        self.driver.find_element(By.XPATH, self.click_proceedtocheckout_xpath).click()

    def  Enter_Firstname(self, Firstname):
        self.driver.find_element(By.XPATH, self.text_Firstname_xpath).send_keys(Firstname)

    def Enter_Lastname(self, Lastname):
        self.driver.find_element(By.XPATH, self.text_lastname_xpath).send_keys(Lastname)

    def Enter_Phone(self, Phone):
        self.driver.find_element(By.XPATH, self.text_phone_xpath).send_keys(Phone)

    def Enter_Address(self, Address):
        self.driver.find_element(By.XPATH, self.text_address_xpath).send_keys(Address)

    def Enter_Zipcode(self, Zipcode):
        self.driver.find_element(By.XPATH, self.text_zipcode_xpath).send_keys(Zipcode)


    def Select_State(self, State):
        dropdown_state = Select(self.driver.find_element(By.XPATH, self.dropdown_state_xpath))
        dropdown_state.select_by_visible_text(State)

    def Enter_Owner(self, Owner):
        self.driver.find_element(By.XPATH, self.text_owner_xpath).send_keys(Owner)

    def Enter_CVV(self, CVV):
        self.driver.find_element(By.XPATH, self.text_cvv_xpath).send_keys(CVV)

    def Enter_CardNumber(self, CardNumber):
        self.driver.find_element(By.XPATH, self.text_CardNumber_xpath).send_keys(CardNumber)

    def Select_Year(self, Year):
        dropdown_year = Select(self.driver.find_element(By.XPATH, self.dropdown_year_xpath))
        dropdown_year.select_by_visible_text(Year)

    def Select_Month(self, Month):
        dropdown_month = Select(self.driver.find_element(By.XPATH, self.dropdown_month_xpath))
        dropdown_month.select_by_visible_text(Month)

    def Click_Checkout(self):
        self.driver.find_element(By.XPATH, self.click_checkout_xpath).click()


    def Verify_Success_Message(self):
       return self.driver.find_element(By.XPATH, self.success_message_xpath).text

    def Get_Order_Number(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.Order_number_css).text

