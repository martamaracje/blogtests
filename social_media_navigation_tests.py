# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep

class social_media_navigation_tests(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_when_clicked_on_facebook_link_then_navigating_to_facebook(self):
        #Arrange
        driver=self.driver
        driver.get("http://martamaracje.blogspot.com")
        expected_url="https://www.facebook.com/martamaracje/"
        social_media_link=driver.find_element_by_css_selector("#fawesomeicons > a[href='" + expected_url + "']")
        initial_tabs=len(driver.window_handles)

        #Act
        social_media_link.click()
        sleep(2) #wait for navigation
        opened_tabs=len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[opened_tabs-1])

        #Assert
        self.assertGreater(opened_tabs, initial_tabs)
        self.assertIn(expected_url, driver.current_url)

    def test_when_clicked_on_twitter_link_then_navigating_to_twitter(self):
        #Arrange
        driver=self.driver
        driver.get("http://martamaracje.blogspot.com")
        expected_url="https://twitter.com/martamaracje/"
        social_media_link=driver.find_element_by_css_selector("#fawesomeicons > a[href='" + expected_url + "']")
        initial_tabs=len(driver.window_handles)

        #Act
        social_media_link.click()
        sleep(2) #wait for navigation
        opened_tabs=len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[opened_tabs-1])

        #Assert
        self.assertGreater(opened_tabs, initial_tabs)
        self.assertIn(expected_url, driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
