from selenium import webdriver
from unittest_kj.com.log_in import *

class CommonMenthod(Login):

    def click(self,list_argument):
        # self.login()
        for item in list_argument:
            self.web.find_element_by_xpath(item).click()

    def send_keys(self,list_address,list_argument):
        # self.login()
        for item in range(len(list_address)):
            self.web.find_element_by_xpath(list_address[item]).clear()
            self.web.find_element_by_xpath(list_address[item]).send_keys(list_argument[item])


