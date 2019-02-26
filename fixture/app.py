from selenium import webdriver
from fixture.role import RoleHelper
from fixture.staff import StaffHelper
from fixture.session import SessionHelper

__author__ = 'andrey'


class Applikation:
    def __init__(self):
        # self.driver = webdriver.Firefox(executable_path=r'D:\GitHub\python_train\driv\geckodriver.exe')
        self.driver = webdriver.Chrome(executable_path=r'D:\GitHub\python_train\driv\chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.staff = StaffHelper(self)
        self.role = RoleHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_page(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.one.comodo.com/app/login")

    def destroy(self):
        self.driver.quit()
