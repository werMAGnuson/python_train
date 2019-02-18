from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
__author__ = 'andrey'


class Applikation:
    def __init__(self):
        # self.driver = webdriver.Firefox(executable_path=r'D:\GitHub\python_train\driv\geckodriver.exe')
        self.driver = webdriver.Chrome(executable_path=r'D:\GitHub\python_train\driv\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    def logout(self):
        driver = self.driver
        driver.find_element_by_id("c1-user-text").click()
        driver.find_element_by_id("c1-menu-logout").click()

    def delite_staff(self):
        driver = self.driver
        driver.find_element_by_class_name("ui-grid-disable-selection").click()
        driver.find_element_by_id("delete-staff-button").click()
        driver.find_element_by_id("c1-popup-ok").click()
        driver.find_element_by_id("c1-popup-ok").click()

    def create_staff(self, staff):
        driver = self.driver
        driver.find_element_by_id("c1-menu-management").click()
        driver.find_element_by_id("c1-menu-staff").click()
        wait = WebDriverWait(driver, 10000)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block-overlay")))
        driver.find_element_by_class_name("fa-plus").click()
        driver.find_element_by_id("add-agent-form-name").send_keys(staff.staff_name)
        driver.find_element_by_id("add-agent-form-email").send_keys(staff.email)
        Select(driver.find_element_by_id("add-agent-form-role")).select_by_visible_text(staff.group_name)
        driver.find_element_by_xpath("//option[@value='4']").click()
        driver.find_element_by_id("save-button-new-staff").click()
        driver.find_element_by_id("c1-popup-ok").click()

    def login(self, user_email, password):
        driver = self.driver
        #driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").send_keys(user_email)
        driver.find_element_by_id("password").send_keys(password)
        # driver.find_element_by_id("password").click()
        driver.find_element_by_xpath("//input[@value='SIGN IN']").click()

    def open_page(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.one.comodo.com/app/login")

    def destroy(self):
        self.driver.quit()