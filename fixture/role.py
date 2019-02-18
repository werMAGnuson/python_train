from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class RoleHelper:
    def __init__(self, app):
        self.app = app

    def opan_to_roles(self):
        driver = self.app.driver
        driver.find_element_by_id("c1-menu-management").click()
        driver.find_element_by_id("c1-menu-roles").click()
        wait = WebDriverWait(driver, 1000)
        time.sleep(3)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block")))
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block-overlay")))

    def create(self, role):
        driver = self.app.driver
        wait = WebDriverWait(driver, 1000)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block-overlay")))
        driver.find_element_by_xpath("//div[contains(text(),'MSP Admin')]").click()
        driver.find_element_by_id("clone-staff-button").click()
        self.role_description(role)
        driver.find_element_by_xpath("//button[contains(text(),'Save Changes')]").click()
        driver.find_element_by_id("c1-popup-ok").click()

    def modify(self, role, role_old):
        driver = self.app.driver
        wait = WebDriverWait(driver, 1000)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block-overlay")))
        driver.find_element_by_xpath("//span[contains(text(),'" + role_old.name + "')]").click()
        driver.find_element_by_id("edit-staff-button").click()
        self.role_description(role)
        driver.find_element_by_xpath("//button[contains(text(),'Save Changes')]").click()
        driver.find_element_by_id("c1-popup-ok").click()

    def role_description(self, role):
        driver = self.app.driver
        if role.definition is not None:
            driver.find_element_by_id("custom-definition").clear()
            driver.find_element_by_id("custom-definition").send_keys(role.definition)
        # el = wait.until(EC.text_to_be_present_in_element((By.ID, "name"),'Admin'))
        if role.name is not None:
            driver.find_element_by_id("name").clear()
            driver.find_element_by_id("name").send_keys(role.name)

    def delite(self, role):
        driver = self.app.driver
        driver.find_element_by_xpath("//span[contains(text(),'" + role.name + "')]").click()
        driver.find_element_by_id("delete-staff-button").click()
        driver.find_element_by_xpath("//button[contains(text(),'Delete')]").click()
        # time.sleep(3)
        wait = WebDriverWait(driver, 1000)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block")))
