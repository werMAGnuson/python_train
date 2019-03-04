from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from model.role import Role


class RoleHelper:
    def __init__(self, app):
        self.app = app

    def open_role_page(self):
        driver = self.app.driver
        if driver.current_url.endswith("/management/role") and len(
                driver.find_elements_by_id("clone-staff-button")) > 0:
            return
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
        self.role_cash = None

    def modify(self, role, role_old):
        driver = self.app.driver
        wait = WebDriverWait(driver, 1000)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block-overlay")))
        driver.find_element_by_xpath("//span[contains(text(),'" + role_old.name + "')]").click()
        driver.find_element_by_id("edit-staff-button").click()
        self.role_description(role)
        driver.find_element_by_xpath("//button[contains(text(),'Save Changes')]").click()
        driver.find_element_by_id("c1-popup-ok").click()
        self.role_cash = None

    def role_is_exists(self, role):
        driver = self.app.driver
        wait = WebDriverWait(driver, 1000)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block-overlay")))

        return len(driver.find_elements_by_xpath("//span[contains(text(),'" + role.name + "')]")) > 0

    def role_description(self, role):
        driver = self.app.driver
        if role.definition is not None:
            driver.find_element_by_id("custom-definition").clear()
            driver.find_element_by_id("custom-definition").send_keys("     ")
            driver.find_element_by_id("custom-definition").clear()
            driver.find_element_by_id("custom-definition").send_keys(role.definition)
        # el = wait.until(EC.text_to_be_present_in_element((By.ID, "name"),'Admin'))
        if role.name is not None:
            driver.find_element_by_id("name").clear()
            driver.find_element_by_id("name").send_keys(role.name)

    def delete(self, role):
        driver = self.app.driver
        driver.find_element_by_xpath("//span[contains(text(),'" + role.name + "')]").click()
        driver.find_element_by_id("delete-staff-button").click()
        driver.find_element_by_xpath("//button[contains(text(),'Delete')]").click()
        # time.sleep(3)
        wait = WebDriverWait(driver, 1000)
        el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block")))
        self.role_cash = None

    role_cash = None

    def get_role_list(self):
        if self.role_cash is None:
            driver = self.app.driver
            self.role_cash = []
            for elements in driver.find_elements_by_css_selector("div.ui-grid-row.ng-scope"):
                name_column = elements.find_element_by_css_selector("span.float-left.ng-binding.ng-scope")#.get_text()
                name = name_column.text
                def_column = elements.find_element_by_css_selector("div.ui-grid-cell-contents.ng-binding.ng-scope")#.get_text()
                definition = def_column.text
                self.role_cash.append(Role(name, definition))
            # for elements in driver.find_elements_by_css_selector("span.float-left.ng-binding.ng-scope"):
            #     text = elements.get_text()

        return list(self.role_cash)

    # def switch_role_page(self):
    #     driver = self.app.driver
    #
    #     wait = WebDriverWait(driver, 1000)
    #     el = wait.until(EC.invisibility_of_element((By.CLASS_NAME, "c1-block")))
