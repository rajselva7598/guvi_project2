import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

class Flipkart(unittest.TestCase):
    def setUp(self):
        global driver
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")

    def test_flipkart(cls):
        cls.driver.get('https://www.flipkart.com')
        print(cls.driver.current_url)
        time.sleep(3)
        cls.assertEqual(cls.driver.current_url, 'https://www.flipkart.com/')

    def test_titleofpage(self):
        self.driver.get('https://www.flipkart.com')
        print(self.driver.current_url)
        time.sleep(3)
        move_to_mainpage = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/button').click()
        time.sleep(3)
        search_input = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        time.sleep(4)
        search_input.send_keys("laptops")

    def test_titleofpage_phone(self):
        self.driver.get('https://www.flipkart.com')
        print(self.driver.current_url)
        time.sleep(3)
        move_to_mainpage = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/button').click()
        time.sleep(3)
        search_input = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        time.sleep(4)
        search_input.send_keys("phone")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()