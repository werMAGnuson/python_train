from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




from fixture.staff import StaffHelper
from fixture.session import SessionHelper

__author__ = 'andrey'


class Applikation:
    def __init__(self):
        # self.driver = webdriver.Firefox(executable_path=r'D:\GitHub\python_train\driv\geckodriver.exe')
        self.driver = webdriver.Chrome(executable_path=r'D:\GitHub\python_train\driv\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.staff = StaffHelper(self)

    def open_page(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.one.comodo.com/app/login")

    def destroy(self):
        self.driver.quit()
