#!/usr/bin/env/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class LoginCheckTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://systers.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_successful_login_check(self):
        driver = self.driver
        driver.get(self.base_url + "/systers-dev/doku.php/gsocstudents2014?do=login")
        driver.find_element_by_id("focus__this").clear()
        driver.find_element_by_id("focus__this").send_keys("username1")
        driver.find_element_by_name("p").clear()
        driver.find_element_by_name("p").send_keys("password1")
        driver.find_element_by_css_selector("fieldset > input.button").click()
        src = driver.page_source
        text_found = re.search(r'Systers Google Summer of Code 2014 - Students Information Page', src)
        self.assertNotEqual(text_found, None)
        
    def test_failing_login_check(self):
        driver = self.driver
        driver.get(self.base_url + "/systers-dev/doku.php/gsocstudents2014?do=login")
        driver.find_element_by_id("focus__this").clear()
        driver.find_element_by_id("focus__this").send_keys("username1")
        driver.find_element_by_name("p").clear()
        driver.find_element_by_name("p").send_keys("password1")
        driver.find_element_by_css_selector("fieldset > input.button").click()
        src = driver.page_source
        text_found = re.search(r'Systers Google Summer of Code 2014 - Students Information Page', src)
        self.assertEqual(text_found, None)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
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
