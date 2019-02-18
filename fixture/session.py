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