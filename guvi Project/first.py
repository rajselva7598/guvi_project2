import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer

driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
class Amazon:
    '''create a class for the Amazon webpage'''
    def get_laptops(self):
        '''This is the method to get the laptops for a particular category'''
        driver.maximize_window()                                                                                                  #maximize the window
        driver.get('https://www.amazon.in')
        time.sleep(3)
        search_input = driver.find_element(by=By.XPATH, value='//*[@id="twotabsearchtextbox"]')
        #search the element the input element by the name of laptops
        search_input.send_keys("laptops")
        time.sleep(3)
        search_btn = driver.find_element(by=By.XPATH, value='//*[@id="nav-search-submit-button"]')
        search_btn.click()
        time.sleep(3)
        input_Search = driver.find_element(by=By.XPATH,
                                           value='//*[@id="p_n_feature_thirteen_browse-bin/12598162031"]/span/a/span').click()
        time.sleep(3)

        hardisk_capacity_Type = driver.find_element(by=By.XPATH,
                                                    value='//*[@id="p_n_pattern_browse-bin/8609969031"]/span/a/span').click()
        time.sleep(5)
        ram_Capactity = driver.find_element(by=By.XPATH,
                                            value='//*[@id="p_n_feature_twenty-six_browse-bin/27399070031"]/span/a/span').click()
        time.sleep(3)
        print(driver.current_url)
        data = requests.get(
            'https://www.amazon.in/s?k=laptops&i=computers&rh=n%3A1375424031%2Cp_n_feature_thirteen_browse-bin%3A12598162031%2Cp_n_pattern_browse-bin%3A8609969031%2Cp_n_feature_twenty-six_browse-bin%3A27399070031&dc&crid=1HDDPZX93HM9X&qid=1655388704&rnid=27399067031&sprefix=laptops%2Caps%2C563&ref=sr_nr_p_n_feature_twenty-six_browse-bin_3')
        time.sleep(3)

        data = requests.get(driver.current_url)
        time.sleep(3)
        soup = BeautifulSoup(data.content, 'lxml')
        name = soup.find('div', class_='col col-7-12')

        with open('laptops1.csv', 'w', encoding='utf8', newline="") as f:
            thewriter = writer(f)                                                                          #the code for make the csv file in the name of laptops1
            thewriter.writerow(['Brand Name', 'Price_of_the_Component'])
            for data in soup.findAll('div', class_='_3pLy-c row'):
                names = data.find('div', class_='_4rR01T').text.replace('\n', '')
                price = data.find('div', class_='_30jeq3 _1_WHN1').text.replace('\n', '')
                info = [names, price]
                thewriter.writerow(info)

    def find_Phone(self):
        '''This is the method to get the phones for a particular category'''

        driver.get('https://www.amazon.in')
        time.sleep(3)
        btn_All=driver.find_element(by=By.XPATH, value='//*[@id="twotabsearchtextbox"]').send_keys('phones')

        time.sleep(3)

        btn_mobileandlaptops = driver.find_element(by=By.XPATH, value='//*[@id="nav-search-submit-button"]').click()
        time.sleep(3)
        hardisk_List = driver.find_element(by=By.XPATH,
                                           value='//*[@id="p_n_feature_eight_browse-bin/8561112031"]/span/a/span').click()
        time.sleep(3)
        ram_type = driver.find_element(by=By.XPATH,
                                           value='//*[@id="p_n_feature_seven_browse-bin/16757454031"]/span/a/span').click()
        time.sleep(3)
        data_transfer = driver.find_element(by=By.XPATH,
                                       value='//*[@id="p_n_feature_five_browse-bin/8561106031"]/span/a/span').click()

        data = requests.get(driver.current_url)
        time.sleep(3)
        soup = BeautifulSoup(data.content, 'lxml')
        name = soup.find('div', class_='col col-7-12')

        with open('phone1.csv', 'w', encoding='utf8', newline="") as f:
            thewriter = writer(f)                                                                          #the code for make the csv file in the name of laptops1
            thewriter.writerow(['Brand Name', 'Price_of_the_Component'])
            for data in soup.findAll('div', class_='_3pLy-c row'):
                names = data.find('div', class_='_4rR01T').text.replace('\n', '')
                price = data.find('div', class_='_30jeq3 _1_WHN1').text.replace('\n', '')
                info = [names, price]
                thewriter.writerow(info)

createURL = Amazon()
createURL.get_laptops()
createURL.find_Phone()
