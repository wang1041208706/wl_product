from selenium import webdriver
import time
from unittest_kj.env.env_factory import *
from ddt import ddt,data
from unittest_kj.test_data.read_data import *

class Login():

    def login(self):
        self.web = webdriver.Firefox()
        self.web.implicitly_wait(20)
        self.web.get(ReadConfig().url)
        self.web.find_element_by_xpath('/html/body/div/section/form/div/input[1]').send_keys(ReadConfig().username)
        self.web.find_element_by_xpath('/html/body/div/section/form/div/input[2]').send_keys(ReadConfig().password)
        self.web.find_element_by_xpath('/html/body/div/section/form/div/input[3]').click()

    def click(self, list_argument):
        for item in list_argument:
            self.web.find_element_by_xpath(item).click()

    def send_keys(self, list_address, list_argument):
        for item in range(len(list_address)):
            self.web.find_element_by_xpath(list_address[item]).clear()
            self.web.find_element_by_xpath(list_address[item]).send_keys(list_argument[item])

    def switch_to(self, argument):
        self.web.iframe = self.web.find_elements_by_tag_name(argument)[0]
        self.web.switch_to.frame(self.web.iframe)
