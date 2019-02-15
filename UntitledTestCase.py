# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://staging.one.comodo.com/app/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("!!TEst123")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sprint52stag1msp@yopmail.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_xpath("//input[@value='SIGN IN']").click()
        driver.find_element_by_xpath("//a[@id='c1-menu-management']/span[3]").click()
        driver.find_element_by_id("c1-menu-staff").click()
        driver.find_element_by_id("new-staff-button").click()
        driver.find_element_by_id("add-agent-form-name").click()
        driver.find_element_by_id("add-agent-form-name").click()
        driver.find_element_by_id("add-agent-form-name").clear()
        driver.find_element_by_id("add-agent-form-name").send_keys("somename")
        driver.find_element_by_id("add-agent-form-email").click()
        driver.find_element_by_id("add-agent-form-email").clear()
        driver.find_element_by_id("add-agent-form-email").send_keys("somename@yopmail.com")
        driver.find_element_by_id("add-agent-form-role").click()
        Select(driver.find_element_by_id("add-agent-form-role")).select_by_visible_text("Admin")
        driver.find_element_by_xpath("//option[@value='4']").click()
        driver.find_element_by_id("save-button-new-staff").click()
        driver.find_element_by_id("c1-popup-ok").click()
        driver.find_element_by_xpath("//div[@id='1550158821253-0-uiGrid-0006-cell']/div").click()
        driver.find_element_by_id("delete-staff-button").click()
        driver.find_element_by_id("c1-popup-ok").click()
        driver.find_element_by_id("c1-popup-ok").click()
        driver.find_element_by_xpath("//a[@id='c1-user-text']/span").click()
        driver.find_element_by_xpath("//a[@id='c1-user-text']/span").click()
        driver.find_element_by_id("c1-menu-logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
