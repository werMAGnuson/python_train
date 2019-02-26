#from time import sleep


class SessionHelper():
    def __init__(self, app):
        self.app = app

    def login(self, user_email, password):
        driver = self.app.driver
        self.app.open_page()
        #driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").send_keys(user_email)
        driver.find_element_by_id("password").send_keys(password)
        # driver.find_element_by_id("password").click()
        driver.find_element_by_xpath("//input[@value='SIGN IN']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_id("c1-user-text").click()
        driver.find_element_by_id("c1-menu-logout").click()
        #driver.getCurrentUrl()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()


    def is_logged_in(self):
        driver = self.app.driver
        #sleep(1)
        return len(driver.find_elements_by_id("c1-user-text")) > 0

    def is_logged_in_as(self, user_email):
        driver = self.app.driver
        return driver.find_element_by_id("c1-user-text").get_attribute("title") == user_email

    def ensure_login(self, user_email, password):
        #driver = self.app.driver
        if self.is_logged_in():
                if self.is_logged_in_as(user_email):
                    return
                else:
                    self.logout()
        self.login(user_email, password)