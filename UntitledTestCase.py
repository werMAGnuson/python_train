# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        #binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        #self.driver = webdriver.Firefox(executable_path=r'D:\GitHub\python_train\driv\geckodriver.exe')
        self.driver = webdriver.Chrome(executable_path=r'D:\GitHub\python_train\driv\chromedriver.exe')

        #self.driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        #self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver.implicitly_wait(30)
        #self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.one.comodo.com/app/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("password").send_keys("!!TEst123")
        driver.find_element_by_id("email").send_keys("sprint52stag1msp@yopmail.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_xpath("//input[@value='SIGN IN']").click()
        driver.find_element_by_id("c1-menu-management").click()
        driver.find_element_by_id("c1-menu-staff").click()
        wait = WebDriverWait(driver, 10000)
        el=wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block-overlay")))
        driver.find_element_by_class_name("fa-plus").click()
        driver.find_element_by_id("add-agent-form-name").click()
        driver.find_element_by_id("add-agent-form-name").send_keys("somename")
        driver.find_element_by_id("add-agent-form-email").click()
        #driver.find_element_by_id("add-agent-form-email").clear()
        driver.find_element_by_id("add-agent-form-email").send_keys("somename@yopmail.com")
        driver.find_element_by_id("add-agent-form-role").click()
        Select(driver.find_element_by_id("add-agent-form-role")).select_by_visible_text("Admin")
        driver.find_element_by_xpath("//option[@value='4']").click()
        driver.find_element_by_id("save-button-new-staff").click()
        driver.find_element_by_id("c1-popup-ok").click()
        driver.find_element_by_class_name("ui-grid-disable-selection").click()
        driver.find_element_by_id("delete-staff-button").click()
        driver.find_element_by_id("c1-popup-ok").click()
        driver.find_element_by_id("c1-popup-ok").click()
        driver.find_element_by_id("c1-user-text").click()
        driver.find_element_by_id("c1-menu-logout").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
