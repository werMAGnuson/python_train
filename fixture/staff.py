import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class StaffHelper:
    def __init__(self, app):
        self.app = app

    def delite(self):
        driver = self.app.driver
        driver.find_element_by_class_name("ui-grid-disable-selection").click()
        driver.find_element_by_id("delete-staff-button").click()
        driver.find_element_by_id("c1-popup-ok").click()
        driver.find_element_by_id("c1-popup-ok").click()

    def create(self, staff):
        driver = self.app.driver
        driver.find_element_by_id("c1-menu-management").click()
        driver.find_element_by_id("c1-menu-staff").click()
        wait = WebDriverWait(driver, 10000)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block-overlay")))
        time.sleep(2)
        #driver.find_element_by_class_name("fa-plus").click()
        #driver.find_element_by_xpath("//button[contains(text(),'New Staff')]").click()
        driver.find_element_by_id("new-staff-button").click()
        driver.find_element_by_id("add-agent-form-name").send_keys(staff.staff_name)
        driver.find_element_by_id("add-agent-form-email").send_keys(staff.email)
        Select(driver.find_element_by_id("add-agent-form-role")).select_by_visible_text(staff.group_name)
        driver.find_element_by_xpath("//option[@value='4']").click()
        driver.find_element_by_id("save-button-new-staff").click()
        driver.find_element_by_id("c1-popup-ok").click()
